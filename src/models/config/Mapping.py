from pydantic import BaseModel


class Mapping(BaseModel):
    platform_id: int
    system: str
    path: str
    extensions: tuple[str, ...]