from src.api.romm import RomMApi
from src.payloads.GetRoms import GetRoms

rommApi = RomMApi()
platforms = rommApi.get_platforms()

for platform in platforms:
    print(f"{platform.id} - {platform.name}")

print("-" * 50)

platform = rommApi.get_platform(6)
print(f"{platform.id} - {platform.name}")

payload: GetRoms = GetRoms(platform_id=6)
games = rommApi.get_roms(payload)
print("-" * 50)
print(games)