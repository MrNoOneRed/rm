from pydantic import BaseModel, ConfigDict
from src.models.LaunchboxImage import LaunchboxImage


class RomLaunchboxMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    first_release_date: int | None
    max_players: int
    release_type: str
    cooperative: bool
    youtube_video_id: str
    community_rating: float
    community_rating_count: int
    wikipedia_url: str
    esrb: str
    genres: list[str]
    companies: list[str]
    images: list[LaunchboxImage]