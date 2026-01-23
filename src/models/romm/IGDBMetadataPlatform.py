from pydantic import BaseModel, ConfigDict


class IGDBMetadataPlatform(BaseModel):
    model_config = ConfigDict(extra="ignore")

    igdb_id: int
    name: str