from pydantic import BaseModel, ConfigDict
from src.models.romm.RAGameRomAchievement import RAGameRomAchievement


class RomRAMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    first_release_date: int | None = None
    genres: list[str] | None = None
    companies: list[str] | None = None
    achievements: list[RAGameRomAchievement] | None = None
