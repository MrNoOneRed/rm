from pydantic import BaseModel, Field
from src.models.config import Base, Mapping


class Root(BaseModel):
    base: Base = Field(default_factory=Base)
    mappings: list[Mapping] = Field(default_factory=list)
