from typing import Any, Iterable

import disnake

from models.users.discord import DiscordBinds, dc_users
from models.users.valorant import fullname2puuid, val_users


def rank2num(rankStr: str) -> int:
    ranks = [
        "Iron",
        "Bronze",
        "Silver",
        "Gold",
        "Platinum",
        "Diamond",
        "Ascendant",
        "Immortal",
        "Radiant",
    ]
    if rankStr is None or rankStr == "Unranked":
        return 0
    rank, level = rankStr.split(" ")
    return ranks.index(rank) * 10 + int(level)


def get_rank_order(
    val_users: dict[str, Any], rank_key: str, limit: int
) -> tuple[Iterable[str], Iterable[str]]:
    keys = list(val_users.keys())
    keys.sort(
        key=lambda x: rank2num(val_users[x].__getattribute__(rank_key)), reverse=True
    )
    if limit > 0:
        keys = keys[:limit]
    return map(lambda x: val_users[x].fullname, keys), map(
        lambda x: val_users[x].__getattribute__(rank_key) or "Unranked", keys
    )
