from src.api.romm import RomMApi
from src.config import ConfigMapping, config
from src.payloads.GetRoms import GetRoms
from src.payloads.GetRomsDownload import GetRomsDownload

roms_path = "/userdata/roms"

class Manager:
    rommApi: RomMApi

    def __init__(self):
        self.rommApi = RomMApi()

    def create_mapping(self, platform_id: int, system: str, subpath: list[str]) -> ConfigMapping:
        path = f"{roms_path}/{system}/{"/".join(subpath)}"

        for mapping in config.mappings:
            if mapping.platform_id == platform_id and mapping.path == path:
                return mapping

        mapping: ConfigMapping = ConfigMapping(
            platform_id=platform_id,
            path=path
        )

        config.mappings.append(mapping)
        config.save()

        return mapping

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