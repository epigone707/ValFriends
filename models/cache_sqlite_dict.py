import time
from typing import Any, Callable

from sqlitedict import SqliteDict


class CacheSqliteDict(SqliteDict):
    def __init__(
        self,
        on_expire: Callable[[Any], Any] | None = None,
        expire_time: int = 600,
        *args: Any,
        **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        self.on_expire = super().__getitem__ if on_expire is None else on_expire
        self.expire_time = expire_time
        self.last_fetch_time: dict[Any, float] = {}
        self.cache_data: dict[Any, Any] = {}

    def __setitem__(self, key: Any, value: Any) -> None:
        super().__setitem__(key, value)
        if value is not None:
            self.last_fetch_time[key] = time.time()
        self.cache_data[key] = value

    def __getitem__(self, key: Any) -> Any:
        if key not in self.last_fetch_time:
            self.last_fetch_time[key] = time.time()
        if (
            not self.__contains__(key)
            or time.time() - self.last_fetch_time[key] > self.expire_time
        ):
            res = self.on_expire(key)
            self.__setitem__(key, res)
            return res
        if key not in self.cache_data:
            self.cache_data[key] = super().__getitem__(key)
        return self.cache_data[key]

    def __delitem__(self, key: Any) -> None:
        super().__delitem__(key)
        del self.cache_data[key]
        del self.last_fetch_time[key]

    def expire(self, key: Any) -> None:
        self.last_fetch_time[key] = time.time() - self.expire_time - 1
        self.__setitem__(key, self.on_expire(key))
