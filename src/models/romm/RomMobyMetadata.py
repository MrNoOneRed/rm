from pydantic import BaseModel, ConfigDict
from src.models.romm.MobyMetadataPlatform import MobyMetadataPlatform


class RomMobyMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    moby_score: str
    genres: list[str]
    alternate_titles: list[str]
    platforms: list[MobyMetadataPlatform]
