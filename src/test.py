from src.api.romm import RomMApi
from src.manager import Manager
from src.payloads.GetRoms import GetRoms
from src.payloads.GetRomsDownload import GetRomsDownload

# rommApi = RomMApi()
# platforms = rommApi.get_platforms()
#
# for platform in platforms:
#     print(f"{platform.id} - {platform.name}")
#
# print("-" * 50)
#
# platform = rommApi.get_platform(6)
# print(f"{platform.id} - {platform.name}")

# payload: GetRoms = GetRoms(platform_id=8)
# games = rommApi.get_roms(payload)
# ids = None
# for game in games.items:
#     if ids is None:
#         ids = f"{game.id}"
#     else:
#         ids += f",{game.id}"
# print("-" * 50)
# print(ids)
# print(games)

# payload: GetRomsDownload = GetRomsDownload(rom_ids="102,252,104")
# link = rommApi.get_roms_download(payload)
# print(link)

manager = Manager()
manager.platform_download(8)