from typing import List

import requests
from pydantic import BaseModel

from logger import logger
from models.cache_sqlite_dict import CacheSqliteDict
from models.openapi import V1Account, V1LifetimeMatches, V1LifetimeMatchesItem, V2mmr
from settings import settings


# stats for the user in a match
class ValStats(BaseModel):
    kills: int
    deaths: int
    assists: int
    damage: int  # damage per round
    result: str  # 'Win' or 'Lose'
    agent: str  # agent name


class ValUser(BaseModel):
    puuid: str
    fullname: str
    hrank: str | None = None
    crank: str | None = None
    elo: int | None = None
    recent_stats: List[ValStats] = []
    crank_img: str | None = None


def fetch_user_stats(puuid: str) -> ValUser:
    """
    send GET request to get the most up-to-date stats of a user
    update users
    return the user stats as a dict
    """
    # name, tag = fullname.split("#")

    # get the rank info
    url = f"https://api.henrikdev.xyz/valorant/v2/by-puuid/mmr/na/{puuid}"
    logger.info(f"fetching data from {url}")
    response = requests.get(url)
    logger.debug(response.json())
    v2_mmr = V2mmr(**response.json())

    # get the stats for recent 5 competitive matches
    matches_url = f"https://api.henrikdev.xyz/valorant/v1/by-puuid/lifetime/matches/na/{puuid}?mode=competitive&size=5"
    logger.info(f"fetching data from {matches_url}")
    matches_response = requests.get(matches_url)
    logger.debug(matches_response.json())
    v1_lifetime_matches = V1LifetimeMatches(**matches_response.json())

    # make/update the user profile
    if v2_mmr.status != 200 or v2_mmr.data is None:
        logger.error(f"error getting: {v2_mmr}")
        raise ValueError()
    elif v1_lifetime_matches.status != 200:
        logger.error(f"error getting: {v1_lifetime_matches}")
        raise ValueError()
    data = v2_mmr.data
    val_user = ValUser(puuid=puuid, fullname=f"{data.name}#{data.tag}")
    if data.highest_rank:
        val_user.hrank = data.highest_rank.patched_tier
    if data.current_data:
        val_user.crank = data.current_data.currenttierpatched
        val_user.elo = data.current_data.elo
        if data.current_data.images:
            val_user.crank_img = data.current_data.images.large

    def gen_val_stats(match: V1LifetimeMatchesItem) -> ValStats:
        return ValStats(
            kills=int(match.stats.kills),
            deaths=int(match.stats.deaths),
            assists=int(match.stats.assists),
            damage=int(match.stats.damage.made // (match.teams.red + match.teams.blue)),
            result=["Lose", "Win"][
                match.stats.team == ["Red", "Blue"][match.teams.red < match.teams.blue]
            ],
            agent=match.stats.character.name,
        )

    val_user.recent_stats = [
        gen_val_stats(match) for match in v1_lifetime_matches.data or []
    ]
    return val_user


def fullname2puuid(fullname: str) -> str:
    name, tag = fullname.split("#")
    url = f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}"
    logger.info(f"fetching data from {url}")
    response = requests.get(url)
    logger.debug(response.json())
    v1_account = V1Account(**response.json())
    if v1_account.data is None or v1_account.data.puuid is None:
        raise ValueError()
    return v1_account.data.puuid


val_users = CacheSqliteDict(
    filename=settings.db_filename,
    tablename="val_users",
    autocommit=True,
    on_expire=fetch_user_stats,
    expire_time=settings.expire_time,
)
