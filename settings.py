from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
  token: str = ""
  guild: int = 0
  db_filename: str = "data.sqlite"


settings = Settings()
