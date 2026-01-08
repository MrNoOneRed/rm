from pydantic import BaseModel, ConfigDict

class GetRomsDownload(BaseModel):
    model_config = ConfigDict(extra="ignore")

    rom_ids: str
    filename: str | None = None
