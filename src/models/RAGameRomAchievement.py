from pydantic import BaseModel, ConfigDict


class RAGameRomAchievement(BaseModel):
    model_config = ConfigDict(extra="ignore")

    ra_id: int | None
    title: str | None
    description: str | None
    points: int | None
    num_awarded: int | None
    num_awarded_hardcore: int | None
    badge_id: str | None
    badge_url_lock: str | None
    badge_path_lock: str | None
    badge_url: str | None
    badge_path: str | None
    display_order: int | None
    type: str | None