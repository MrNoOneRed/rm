import sys
from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class ConfigBase(BaseModel):
    romm_base_url: str = ""
    romm_username: str = ""
    romm_password: str = ""

class ConfigMapping(BaseModel):
    platform_id: int
    path: str

class ConfigRoot(BaseModel):
    base: ConfigBase = Field(default_factory=ConfigBase)
    mappings: list[ConfigMapping] = Field(default_factory=list)

class Config(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    root_path: str = "/userdata"
    base: ConfigBase = {}
    mappings: list[ConfigMapping] = []

    def __init__(self):
        super().__init__()

        if len(sys.argv) > 1 and sys.argv[1] == "dev":
            self.root_path = "./data"
        else:
            if not Path(self.root_path).exists():
                raise FileNotFoundError(f"Root path does not exist: {self.root_path}")

        self.load()

    def load(self):
        if not self.path().exists():
            self.save()

        loaded: ConfigRoot = ConfigRoot(base=self.base, mappings=self.mappings)
        loaded = loaded.model_validate_json(self.path().read_text(encoding="utf-8"))

        self.base = loaded.base
        self.mappings = loaded.mappings

    def save(self) -> None:
        self.path().parent.mkdir(parents=True, exist_ok=True)
        self.path().write_text(self.root().model_dump_json(ensure_ascii=False, indent=2), encoding="utf-8")

    def root(self) -> ConfigRoot:
        return ConfigRoot(base=self.base, mappings=self.mappings)

    def path(self) -> Path:
        return Path(f"{self.root_path}/.config/rm/config.json")


config = Config()
