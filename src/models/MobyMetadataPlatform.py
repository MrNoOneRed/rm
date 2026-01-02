from pydantic import BaseModel, ConfigDict


class MobyMetadataPlatform(BaseModel):
    model_config = ConfigDict(extra="ignore")

    moby_id: int
    name: str
