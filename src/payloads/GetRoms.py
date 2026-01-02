from pydantic import BaseModel, ConfigDict

class GetRoms(BaseModel):
    model_config = ConfigDict(extra="ignore")

    with_char_index: bool = True
    search_term: str | None = None
    platform_id: int | None = None
    collection_id: int | None = None
    virtual_collection_id: int | None = None
    smart_collection_id: int | None = None
    matched: bool | None = None
    favorite: bool | None = None
    duplicate: bool | None = None
    playable: bool | None = None
    missing: bool | None = None
    has_ra: bool | None = None
    verified: bool | None = None
    group_by_meta_id: bool = False
    selected_genre: str | None = None
    selected_franchise: str | None = None
    selected_collection: str | None = None
    selected_company: str | None = None
    selected_age_rating: str | None = None
    selected_status: str | None = None
    selected_region: str | None = None
    selected_language: str | None = None
    order_by: str = "name"
    order_dir: str = "asc"
    limit: int = 50
    offset: int = 0