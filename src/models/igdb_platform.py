from pydantic import BaseModel, ConfigDict


class IgdbPlatform(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    name: str