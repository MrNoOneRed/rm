from pydantic import BaseModel, ConfigDict


class LaunchboxImage(BaseModel):
    model_config = ConfigDict(extra="ignore")

    url: str
    type: str
    region: str