from pydantic import BaseModel, ConfigDict


class RomHLTBMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    main_story: int
    main_story_count: int
    main_plus_extra: int
    main_plus_extra_count: int
    completionist: int
    completionist_count: int
    all_styles: int
    all_styles_count: int
    release_year: int
    review_score: int
    review_count: int
    popularity: int
    completions: int


