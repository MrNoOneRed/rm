from pydantic import BaseModel, ConfigDict


class SiblingRomSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    name: str | None
    fs_name_no_tags: str
    fs_name_no_ext: str
    sort_comparator: str
