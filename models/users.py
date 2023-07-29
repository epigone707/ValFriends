import requests

from logger import logger
from settings import settings
from models.cache_sqlite_dict import CacheSqliteDict
from models.openapi import V2mmr, V1LifetimeMatches
from pydantic import BaseModel
from typing import Optional, List
from utils import get_match_result


# stats for the user in a match
class ValStats(BaseModel):
  kills: int
  deaths: int
  assists: int
  damage: int  # damage per round
  result: str  # 'Win' or 'Lose'


class Profile(BaseModel):
  fullname: str
  hrank: Optional[str] = None
  crank: Optional[str] = None
  elo: Optional[int] = None
  recent_stats: List[ValStats] = []


def fetch_user_stats(fullname):
  """
  send GET request to get the most up-to-date stats of a user
  update users
  return the user stats as a dict
  """
  name, tag = fullname.split("#")

  # get the rank info
  url = f"https://api.henrikdev.xyz/valorant/v2/mmr/na/{name}/{tag}"
  logger.info(f"fetching data from {url}")
  response = requests.get(url)
  logger.debug(response.json())
  v2_mmr = V2mmr(**response.json())

  # get the stats for recent 3 competitive matches
  matches_url = f"https://api.henrikdev.xyz/valorant/v1/lifetime/matches/na/{name}/{tag}?mode=competitive&size=3"
  logger.info(f"fetching data from {matches_url}")
  matches_response = requests.get(matches_url)
  logger.debug(matches_response.json())
  v1_lifetime_matches = V1LifetimeMatches(**matches_response.json())

  # make/update the user profile
  profile = Profile(fullname=fullname)  # placeholder
  if v2_mmr.status != 200:
    logger.error(f"error getting: {v2_mmr}")
  elif v1_lifetime_matches.status != 200:
    logger.error(f"error getting: {v1_lifetime_matches}")
  else:
    data = v2_mmr.data
    profile.fullname = f"{data.name}#{data.tag}"
    profile.hrank = data.highest_rank.patched_tier
    profile.crank = data.current_data.currenttierpatched
    profile.elo = data.current_data.elo
    profile.recent_stats = [
      ValStats(kills=match.stats.kills,
               deaths=match.stats.deaths,
               assists=match.stats.assists,
               damage=match.stats.damage.made //
               (match.teams.red + match.teams.blue),
               result=get_match_result(match.stats.team, match.teams.red,
                                       match.teams.blue))
      for match in v1_lifetime_matches.data
    ]
  return profile


class UserDict(CacheSqliteDict):

  def __getitem__(self, key) -> Profile:
    return super().__getitem__(key.lower())

  def __setitem__(self, key, value):
    super().__setitem__(key.lower(), value)

  def __delitem__(self, key):
    super().__delitem__(key.lower())

  def expire(self, key):
    super().expire(key.lower())

  def keys(self):
    for k in super().keys():
      yield super().__getitem__(k).fullname

  def items(self):
    for k, v in super().items():
      yield super().__getitem__(k).fullname, v


users = UserDict(filename=settings.db_filename,
                 tablename="users",
                 autocommit=True,
                 on_expire=fetch_user_stats,
                 expire_time=settings.expire_time)
