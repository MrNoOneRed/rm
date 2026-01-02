from datetime import datetime
from pydantic import BaseModel, ConfigDict
from src.models.FirmwareSchema import FirmwareSchema


class PlatformSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    slug: str
    fs_slug: str
    rom_count: int
    name: str
    igdb_slug: str | None
    moby_slug: str | None
    hltb_slug: str | None
    custom_name: str | None
    igdb_id: int | None
    sgdb_id: int | None
    moby_id: int | None
    launchbox_id: int | None
    ss_id: int | None
    ra_id: int | None
    hasheous_id: int | None
    tgdb_id: int | None | None
    flashpoint_id: int | None | None
    category: str | None
    generation: int | None
    family_name: str | None
    family_slug: str | None
    url: str | None
    url_logo: str | None
    firmware: list[FirmwareSchema] = []
    aspect_ratio: str = "2/3"
    created_at: datetime
    updated_at: datetime
    fs_size_bytes: int
    is_unidentified: bool
    is_identified: bool
    missing_from_fs: bool
    display_name: str