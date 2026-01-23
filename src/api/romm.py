from typing import Callable

import httpx

from urllib.parse import unquote
from pydantic import TypeAdapter
from src.config import config
from src.models.romm.CustomLimitOffsetPage import CustomLimitOffsetPage
from src.models.romm.PlatformSchema import PlatformSchema
from src.payloads.GetRoms import GetRoms
from src.payloads.GetRomsDownload import GetRomsDownload


class RomMApi:

    def __init__(self, timeout: float = 120.0):
        self.headers = {"Accept": "application/json"}
        self.client = httpx.Client(
            base_url=config.base.romm_base_url,
            headers=self.headers,
            timeout=timeout,
            auth=httpx.BasicAuth(username=config.base.romm_username, password=config.base.romm_password)
        )

    def get_platforms(self) -> list[PlatformSchema]:
        response = self.client.get("/platforms")
        response.raise_for_status()

        return TypeAdapter(list[PlatformSchema]).validate_python(response.json())

    def get_platform(self, platform_id: int) -> PlatformSchema:
        response = self.client.get(f"/platforms/{platform_id}")
        response.raise_for_status()

        return PlatformSchema.model_validate(response.json())

    def get_roms(self, payload: GetRoms) -> CustomLimitOffsetPage:
        params = payload.model_dump(exclude_none=True)
        response = self.client.get(url=f"/roms", params=params)
        response.raise_for_status()

        return CustomLimitOffsetPage.model_validate(response.json())

    def get_roms_download(self, payload: GetRomsDownload, progress: Callable | None = None) -> str:
        params = payload.model_dump(exclude_none=True)

        with self.client.stream("GET", url=f"/roms/download", params=params, timeout=None) as response:
            response.raise_for_status()
            cd = response.headers.get("content-disposition", "")
            total = int(response.headers.get("content-length", 0))
            offset = 0
            filename = "roms.zip"

            if "filename=" in cd:
                filename = unquote(cd.split("filename=")[-1].strip('"'))

            path = f"./data/tmp/{filename}"

            with open(path, "wb") as f:
                for chunk in response.iter_bytes(1024 * 1024):
                    f.write(chunk)
                    offset += len(chunk)

                    if progress:
                        progress("Downloading games: ", offset, total, True)

                if progress:
                    progress("Downloading games: ", total, total)

            return path
