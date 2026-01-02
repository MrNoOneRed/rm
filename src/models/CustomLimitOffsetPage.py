from pydantic import BaseModel, ConfigDict
from src.models.SimpleRomSchema import SimpleRomSchema


class CustomLimitOffsetPage(BaseModel):
    model_config = ConfigDict(extra="ignore")

    items: list[SimpleRomSchema]
    total: int
    limit: int
    offset: int
    char_index: dict[str,int]
    rom_id_index: list[int]
