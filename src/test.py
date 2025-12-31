from src.api.romm import RomMApi

rommApi = RomMApi()
platforms = rommApi.get_platforms()

for platform in platforms:
    print(f"{platform.id} - {platform.name}")

print("-" * 50)

platform = rommApi.get_platform(6)
print(f"{platform.id} - {platform.name}")