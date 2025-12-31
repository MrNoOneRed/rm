from pydantic import BaseModel, ConfigDict

from src.models.age_rating import AgeRating
from src.models.igdb_platform import IgdbPlatform


class IgbdMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    total_rating: str
    aggregated_rating: str
    first_release_date: int
    youtube_video_id: str
    genres: list[str]
    franchises: list[str]
    alternative_names: list[str]
    collections: list[str]
    companies: list[str]
    game_modes: list[str]
    age_ratings: list[AgeRating]
    platforms: list[IgdbPlatform]

    # expansions: List[RelatedGame]
    # dlcs: List[RelatedGame]
    # remasters: List[RelatedGame]
    # remakes: List[RelatedGame]
    # expanded_games: List[RelatedGame]
    # ports: List[RelatedGame]
    # similar_games: List[RelatedGame]