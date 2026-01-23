from pydantic import BaseModel


class GameShort(BaseModel):
    romm_id: int | None = None
    name: str | None = None
    crc: str | None = None
    md5: str | None = None
    sha1: str | None = None
    size: int = 0
    local_path: str | None = None

    def set_local_path(self, path: str):
        self.local_path = path