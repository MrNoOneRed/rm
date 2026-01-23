from pydantic import BaseModel, ConfigDict


class IGDBRelatedGame(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    name: str
    slug: str
    type: str
    cover_url: str