from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", )

    romm_base_url: str = ""
    romm_username: str = ""
    romm_password: str = ""

config = Config()