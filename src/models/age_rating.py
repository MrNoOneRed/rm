from pydantic import BaseModel, ConfigDict


class AgeRating(BaseModel):
    model_config = ConfigDict(extra="ignore")

    rating: str
    category: str
    rating_cover_url: str