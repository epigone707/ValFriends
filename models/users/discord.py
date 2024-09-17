from typing import List
from pydantic import BaseModel

from models.cache_sqlite_dict import CacheSqliteDict
from models.users.valorant import ValStats, ValUser, val_users, val_user_stats
from settings import settings


class DCUser(BaseModel):
    val_id: str = ""

    @property
    def val_user(self) -> ValUser:
        return val_users[self.val_id]

    @property
    def val_user_stats(self) -> List[ValStats]:
        return val_user_stats[self.val_id]


dc_users = CacheSqliteDict(
    filename=settings.db_filename,
    tablename="dc_users",
    autocommit=True,
)
