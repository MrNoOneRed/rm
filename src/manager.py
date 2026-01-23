import sys
from pprint import pprint

import math

from pathlib import Path
from typing import Callable
from src.api.romm import RomMApi
from src.config import config
from src.models.GameShort import GameShort
from src.models.MappingGamesResult import MappingGamesResult
from src.models.config import Mapping
from src.payloads.GetRoms import GetRoms
from src.payloads.GetRomsDownload import GetRomsDownload
from src.services import Terminal
from src.services.file_manager import FileManager

romm_limit = 100

class Manager:
    rommApi: RomMApi

    def __init__(self):
        self.rommApi = RomMApi()

    @staticmethod
    def mapping_create(platform_id: int, system: str, extensions: tuple[str, ...], subpath: list[str] | None = None) -> Mapping:
        path = Path(f"{config.root_path}/roms/{system}")

        if subpath is not None and len(subpath) > 0:
            path = path / f"{"/".join(subpath)}"

        for mapping in config.mappings:
            if mapping.platform_id == platform_id and mapping.path == path.__str__():
                return mapping

        path.mkdir(parents=True, exist_ok=True)

        mapping: Mapping = Mapping(
            platform_id=platform_id,
            system=system,
            extensions=extensions,
            path=path.__str__()
        )

        config.mappings.append(mapping)
        config.save()

        return mapping

    def get_romm_games(self, platform_id: int, limit: int = 100, progress: Callable | None = None) -> list[GameShort]:
        platform = self.rommApi.get_platform(platform_id)
        pages = math.ceil(platform.rom_count / limit)
        romm_games: list[GameShort] = []

        for page in range(pages):
            offset = page * limit
            payload = GetRoms(platform_id=platform_id, limit=limit, offset=offset)
            games = self.rommApi.get_roms(payload)

            for item in games.items:
                game: GameShort = GameShort(
                    romm_id=item.id,
                    name=item.fs_name,
                    crc=item.crc_hash,
                    md5=item.md5_hash,
                    sha1=item.sha1_hash,
                    size=item.fs_size_bytes
                )

                romm_games.append(game)
            progress("Read romm games: ", offset, platform.rom_count, True)

        progress("Read romm games: ", platform.rom_count, platform.rom_count)

        return romm_games

    @staticmethod
    def get_local_games(path: str, limit: int = 100, progress: Callable | None = None) -> list[GameShort]:
        total = FileManager.file_count(path)
        offset = 0
        path = Path(path)
        games: list[GameShort] = []

        for file in path.iterdir():
            if file.is_dir():
                continue

            hashes = FileManager.file_hashes(file)

            game: GameShort = GameShort(
                local_path=file.resolve().__str__(),
                name=file.name,
                crc=hashes.crc if hashes is not None else None,
                md5=hashes.md5 if hashes is not None else None,
                sha1=hashes.sha1 if hashes is not None else None,
                size=file.stat().st_size
            )

            progress("Read local games: ", offset, total, True)

            offset += 1

            games.append(game)

        progress("Read local games: ", total, total)

        return games

    def mapping_calculate(self, mapping: Mapping) -> MappingGamesResult:
        romm_games = self.get_romm_games(mapping.platform_id, romm_limit, Terminal.progress_bar)
        local_games = self.get_local_games(mapping.path, romm_limit, Terminal.progress_bar)

        games: MappingGamesResult = MappingGamesResult()

        for romm_game in romm_games:
            match = False

            for local_game in local_games:
                if romm_game.name == local_game.name and romm_game.crc == local_game.crc and romm_game.md5 == local_game.md5 and romm_game.sha1 == local_game.sha1 and romm_game.size == local_game.size:
                    match = True
                    break

            if not match:
                games.new.append(romm_game)

        for local_game in local_games:
            match = False

            if local_game.crc is None or local_game.md5 is None or local_game.sha1 is None:
                games.remove.append(local_game)

                for new_game in games.new:
                    if new_game.name == local_game.name and new_game.size == local_game.size:
                        games.new.remove(new_game)

                continue

            for romm_game in romm_games:
                if romm_game.name == local_game.name and romm_game.crc == local_game.crc and romm_game.md5 == local_game.md5 and romm_game.sha1 == local_game.sha1 and romm_game.size == local_game.size:
                    match = True
                    break

            if not match:
                games.remove.append(local_game)

        return games

    def mapping_games_download(self, mapping: Mapping, games: list[GameShort]):
        if len(games) > 0:
            payload = GetRomsDownload(rom_ids=",".join([str(game.romm_id) for game in games]))
            path = self.rommApi.get_roms_download(payload, Terminal.progress_bar)
            FileManager.files_unzip(path, mapping.path, Terminal.progress_bar)

    def platform_download(self, platform_id: int):
        limit = 1
        offset = 0

        games = self.rommApi.get_roms(GetRoms(platform_id=platform_id, limit=limit, offset=offset))
        path = self.rommApi.get_roms_download(
            GetRomsDownload(rom_ids=",".join([str(rom_id) for rom_id in games.rom_id_index])))

        print(f"limit: {games.limit}")
        print(f"total: {games.total}")
        print(f"offset: {games.offset}")
        print(f"offset: {len(games.rom_id_index)}")
        pass
