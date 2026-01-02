import httpx

from pydantic import TypeAdapter
from src.config import config
from src.models.CustomLimitOffsetPage import CustomLimitOffsetPage
from src.models.PlatformSchema import PlatformSchema
from src.payloads.GetRoms import GetRoms


class RomMApi:

    def __init__(self, timeout: float = 10.0):
        self.headers = {"Accept": "application/json"}
        self.client = httpx.Client(
            base_url=config.romm_base_url,
            headers=self.headers,
            timeout=timeout,
            auth=httpx.BasicAuth(username=config.romm_username, password=config.romm_password)
        )

    def get_platforms(self) -> list[PlatformSchema]:
        response = self.client.get("/platforms")
        response.raise_for_status()


        return TypeAdapter(list[PlatformSchema]).validate_python(response.json())

    def get_platform(self, platform_id: int) -> PlatformSchema:
        response = self.client.get(f"/platforms/{platform_id}")
        response.raise_for_status()

        return PlatformSchema.model_validate(response.json())

    # TODO: Dokonczyc problemy z typowaniem danych romow

    def get_roms(self, payload: GetRoms) -> CustomLimitOffsetPage:
        response = self.client.get(f"/roms")
        response.raise_for_status()

        return CustomLimitOffsetPage.model_validate(response.json())