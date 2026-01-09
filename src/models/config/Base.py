from pydantic import BaseModel


class Base(BaseModel):
    romm_base_url: str = ""
    romm_username: str = ""
    romm_password: str = ""