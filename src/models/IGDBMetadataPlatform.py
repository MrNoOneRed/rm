from pydantic import BaseModel, ConfigDict


class IGDBMetadataPlatform(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    name: str