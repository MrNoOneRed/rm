import httpx

from pydantic import TypeAdapter
from src.config import config
from src.models.platform import Platform
from src.payloads.get_roms import GetRoms


class RomMApi:

    def __init__(self, timeout: float = 10.0):
        self.headers = {"Accept": "application/json"}
        self.client = httpx.Client(
            base_url=config.romm_base_url,
            headers=self.headers,
            timeout=timeout,
            auth=httpx.BasicAuth(username=config.romm_username, password=config.romm_password)
        )

    def get_platforms(self) -> list[Platform]:
        response = self.client.get("/platforms")
        response.raise_for_status()


        return TypeAdapter(list[Platform]).validate_python(response.json())

    def get_platform(self, platform_id: int) -> Platform:
        response = self.client.get(f"/platforms/{platform_id}")
        response.raise_for_status()

        return Platform.model_validate(response.json())

    ## TODO: dokonczyc modele dla endpointu get_roms

    def get_roms(self, payload: GetRoms) -> Platform:
        pass
        # response = self.client.get(f"/platforms/{platform_id}")
        # response.raise_for_status()
        #
        # return Platform.model_validate(response.json())