from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
  token: str = ""
  guild: int = 0
  db_filename: str = "data.sqlite"
  expire_time: int = 60 * 60
  log_filename: str = "val-friend.log"
  test_server_id: int = 0


settings = Settings()
