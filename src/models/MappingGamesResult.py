from pydantic import BaseModel
from src.models.GameShort import GameShort

class MappingGamesResult(BaseModel):
    new: list[GameShort] = []
    overwrite: list[GameShort] = []
    remove: list[GameShort] = []
