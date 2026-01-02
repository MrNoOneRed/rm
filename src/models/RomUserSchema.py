from datetime import datetime
from pydantic import BaseModel, ConfigDict


class RomUserSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    user_id: int
    rom_id: int
    created_at: datetime
    updated_at: datetime
    last_played: str | None
    is_main_sibling: bool
    backlogged: bool
    now_playing: bool
    hidden: bool
    rating: int
    difficulty: int
    completion: int
    status: str | None
    user__username: str