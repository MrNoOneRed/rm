from pydantic import BaseModel, ConfigDict


class RomSSMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    bezel_url: str | None
    box2d_url: str | None
    box2d_side_url: str | None
    box2d_back_url: str | None
    box3d_url: str | None
    fanart_url: str | None
    fullbox_url: str | None
    logo_url: str | None
    manual_url: str | None
    marquee_url: str | None
    miximage_url: str | None
    physical_url: str | None
    screenshot_url: str | None
    steamgrid_url: str | None
    title_screen_url: str | None
    video_url: str | None
    video_normalized_url: str | None
    bezel_path: str | None
    box2d_back_path: str | None
    box3d_path: str | None
    fanart_path: str | None
    miximage_path: str | None
    physical_path: str | None
    marquee_path: str | None
    logo_path: str | None
    video_path: str | None
    ss_score: str
    first_release_date: int | None
    alternative_names: list[str]
    companies: list[str]
    franchises: list[str]
    game_modes: list[str]
    genres: list[str]
