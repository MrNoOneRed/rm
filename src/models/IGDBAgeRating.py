from pydantic import BaseModel, ConfigDict


class IGDBAgeRating(BaseModel):
    model_config = ConfigDict(extra="ignore")

    rating: str
    category: str
    rating_cover_url: str