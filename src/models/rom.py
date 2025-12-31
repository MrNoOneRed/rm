from pydantic import BaseModel, ConfigDict

from src.models.platform import Platform


class Rom(BaseModel):
    model_config = ConfigDict(extra="ignore")

    platforms: list[Platform]