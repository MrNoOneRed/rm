from pydantic import BaseModel, ConfigDict


class RomHLTBMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    main_story: int | None = None
    main_story_count: int | None = None
    main_plus_extra: int | None = None
    main_plus_extra_count: int | None = None
    completionist: int | None = None
    completionist_count: int | None = None
    all_styles: int | None = None
    all_styles_count: int | None = None
    release_year: int | None = None
    review_score: int | None = None
    review_count: int | None = None
    popularity: int | None = None
    completions: int | None = None


