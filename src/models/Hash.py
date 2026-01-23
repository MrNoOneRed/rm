from pydantic import BaseModel

class Hash(BaseModel):
    crc: str
    md5: str
    sha1: str
