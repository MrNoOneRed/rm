from typing import Annotated
from pydantic import BaseModel, ConfigDict, BeforeValidator
from src.models.IGDBAgeRating import IGDBAgeRating
from src.models.IGDBMetadataPlatform import IGDBMetadataPlatform
from src.models.IGDBRelatedGame import IGDBRelatedGame
from src.validators.modelValidators import empty_dict_to_none


class RomIGDBMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    total_rating: str
    aggregated_rating: str
    first_release_date: int | None
    youtube_video_id: str | None
    genres: list[str]
    franchises: list[str]
    alternative_names: list[str]
    collections: list[str]
    companies: list[str]
    game_modes: list[str]
    age_ratings: list[IGDBAgeRating]
    platforms: Annotated[list[IGDBMetadataPlatform] | None, BeforeValidator(empty_dict_to_none)]
    expansions: list[IGDBRelatedGame]
    dlcs: list[IGDBRelatedGame]
    remasters: list[IGDBRelatedGame]
    remakes: list[IGDBRelatedGame]
    expanded_games: list[IGDBRelatedGame]
    ports: list[IGDBRelatedGame]
    similar_games: list[IGDBRelatedGame]