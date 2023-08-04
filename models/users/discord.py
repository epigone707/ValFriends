from pydantic import BaseModel

from models.cache_sqlite_dict import CacheSqliteDict
from models.users.valorant import ValUser, val_users
from settings import settings


class DCUser(BaseModel):
    val_id: str = ""

    @property
    def val_user(self) -> ValUser:
        return val_users[self.val_id]


dc_users = CacheSqliteDict(
    filename=settings.db_filename,
    tablename="dc_users",
    autocommit=True,
)
