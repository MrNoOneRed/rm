from pydantic import BaseModel, ConfigDict


class RomFlashpointMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    franchises: list[str]
    companies: list[str]
    source: str
    genres: list[str]
    first_release_date: str
    game_modes: list[str]
    status: str
    version: str
    language: str
    notes: str

