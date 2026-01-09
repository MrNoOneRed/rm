from pydantic import BaseModel, Field


class System(BaseModel):
    name: str
    extensions: tuple[str, ...]

class Systems(BaseModel):
    snes: System = Field(default_factory=System)
    channelf: System = Field(default_factory=System)

systems = Systems(
    snes=System(name="snes", extensions=("smc", "fig", "sfc", "gd3", "gd7", "dx2", "bsx", "swc", "zip", "7z")),
    channelf=System(name="channelf", extensions=("zip", "rom", "bin", "chf"))
)
