from pydantic import BaseModel, ConfigDict


class RomGamelistMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    box2d_url: str | None
    box2d_back_url: str | None
    box3d_url: str | None
    fanart_url: str | None
    image_url: str | None
    manual_url: str | None
    marquee_url: str | None
    miximage_url: str | None
    physical_url: str | None
    screenshot_url: str | None
    thumbnail_url: str | None
    title_screen_url: str | None
    video_url: str | None
    rating: float | None
    first_release_date: str | None
    companies: list[str] | None
    franchises: list[str] | None
    genres: list[str] | None
    player_count: str | None
    md5_hash: str | None
    box3d_path: str | None
    miximage_path: str | None
    physical_path: str | None
    marquee_path: str | None
    video_path: str | None