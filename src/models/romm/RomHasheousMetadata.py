from pydantic import BaseModel, ConfigDict


class RomHasheousMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    tosec_match: bool
    mame_arcade_match: bool
    mame_mess_match: bool
    nointro_match: bool
    redump_match: bool
    whdload_match: bool
    ra_match: bool
    fbneo_match: bool
    puredos_match: bool

