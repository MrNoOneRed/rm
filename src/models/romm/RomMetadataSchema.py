from pydantic import BaseModel, ConfigDict


class RomMetadataSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")

    rom_id: int
    genres: list[str]
    franchises: list[str]
    collections: list[str]
    companies: list[str]
    game_modes: list[str]
    age_ratings: list[str]
    first_release_date: int | None
    average_rating: float | None