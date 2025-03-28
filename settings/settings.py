import os
from pydantic_settings import BaseSettings, SettingsConfigDict

env = os.getenv("ENV", "qa")

env_file = os.path.join(os.path.dirname(__file__), f".{env}.env")


class StackSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding="utf-8")

    TABLE_NAME: str
    POINT_IN_TIME_RECOVERY: bool
