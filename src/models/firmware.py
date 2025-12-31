from datetime import datetime
from pydantic import BaseModel, ConfigDict

class Firmware(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    file_name: str
    file_name_no_tags: str
    file_name_no_ext: str
    file_extension: str
    file_path: str
    file_size_bytes: int
    full_path: str
    is_verified: bool
    crc_hash: str
    md5_hash: str
    sha1_hash: str
    missing_from_fs: bool
    created_at: datetime
    updated_at: datetime