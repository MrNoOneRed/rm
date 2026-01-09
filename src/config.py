import sys
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.models.config import Base, Mapping, Root


class Config(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    root_path: str = "/userdata"
    base: Base = {}
    mappings: list[Mapping] = []

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

        loaded = self.root()
        loaded = loaded.model_validate_json(self.path().read_text(encoding="utf-8"))

        self.base = loaded.base
        self.mappings = loaded.mappings

    def save(self) -> None:
        self.path().parent.mkdir(parents=True, exist_ok=True)
        self.path().write_text(self.root().model_dump_json(ensure_ascii=False, indent=2), encoding="utf-8")

    def root(self) -> Root:
        return Root(base=self.base, mappings=self.mappings)

    def path(self) -> Path:
        return Path(f"{self.root_path}/.config/rm/config.json")


config = Config()
