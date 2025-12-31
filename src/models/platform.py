from datetime import datetime
from pydantic import BaseModel, ConfigDict
from src.models.firmware import Firmware

class Platform(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    slug: str
    fs_slug: str
    rom_count: int
    name: str

    igdb_slug: str
    moby_slug: str
    hltb_slug: str | None
    custom_name: str

    igdb_id: int
    sgdb_id: int | None
    moby_id: int
    launchbox_id: int
    ss_id: int
    ra_id: int
    hasheous_id: int
    tgdb_id: int | None
    flashpoint_id: int | None

    category: str
    generation: int
    family_name: str
    family_slug: str

    url: str
    url_logo: str

    firmware: list[Firmware] = []

    aspect_ratio: str
    created_at: datetime
    updated_at: datetime

    fs_size_bytes: int
    is_unidentified: bool
    is_identified: bool
    missing_from_fs: bool
    display_name: str