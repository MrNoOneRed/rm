from pathlib import Path

from src.api.romm import RomMApi
from src.config import config
from src.models.config import Mapping
from src.payloads.GetRoms import GetRoms
from src.payloads.GetRomsDownload import GetRomsDownload

class Manager:
    rommApi: RomMApi

    def __init__(self):
        self.rommApi = RomMApi()

    @staticmethod
    def create_mapping(platform_id: int, system: str, extensions: tuple[str, ...], subpath: list[str] | None = None) -> Mapping:
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

    def check_mapping(self, mapping: Mapping) -> None:
        platform = self.rommApi.get_platform(mapping.platform_id)


    def platform_download(self, platform_id: int):
        limit = 1
        offset = 0

        games = self.rommApi.get_roms(GetRoms(platform_id=platform_id, limit=limit, offset=offset))
        path = self.rommApi.get_roms_download(GetRomsDownload(rom_ids=",".join([str(rom_id) for rom_id in games.rom_id_index])))


        print(f"limit: {games.limit}")
        print(f"total: {games.total}")
        print(f"offset: {games.offset}")
        print(f"offset: {len(games.rom_id_index)}")
        pass