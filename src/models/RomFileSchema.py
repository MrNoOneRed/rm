from datetime import datetime
from pydantic import BaseModel, ConfigDict


class RomFileSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    rom_id: int
    file_name: str
    file_path: str
    file_size_bytes: int
    full_path: str
    created_at: datetime
    updated_at: datetime
    last_modified: datetime
    crc_hash: str | None
    md5_hash: str | None
    sha1_hash: str | None
    category: str | None



