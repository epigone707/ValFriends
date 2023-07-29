from sqlitedict import SqliteDict
import time

class CacheSqliteDict(SqliteDict):

  def __init__(self, on_expire, expire_time, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.on_expire = on_expire
    self.expire_time = expire_time
    self.last_fetch_time = {}
    self.cache_data = {}

  def __setitem__(self, key, value):
    super().__setitem__(key, value)
    if value is not None:
      self.last_fetch_time[key] = time.time()
    self.cache_data[key] = value
  
  def __getitem__(self, key):
    if key not in self.last_fetch_time:
      self.last_fetch_time[key] = time.time()
    if not self.__contains__(
        key) or time.time() - self.last_fetch_time[key] > self.expire_time:
      res = self.on_expire(key)
      self.__setitem__(key, res)
      return res
    if key not in self.cache_data:
      self.cache_data[key] = super().__getitem__(key)
    return self.cache_data[key]

  def __delitem__(self, key):
    super().__delitem__(key)
    del self.cache_data[key]
    del self.last_fetch_time[key]

  def expire(self, key):
    self.last_fetch_time[key] = time.time() - self.expire_time - 1
    self.__setitem__(key, self.on_expire(key))
