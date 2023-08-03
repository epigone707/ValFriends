from typing import Any, Iterable


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
    users: dict[str, Any], rank_key: str, limit: int
) -> tuple[list[str], Iterable[str]]:
    userList = list(users.keys())
    userList.sort(
        key=lambda x: rank2num(users[x].__getattribute__(rank_key)), reverse=True
    )
    if limit > 0:
        userList = userList[:limit]
    return userList, map(
        lambda x: users[x].__getattribute__(rank_key) or "Unranked", userList
    )
