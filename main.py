import asyncio
from datetime import datetime
import time
import traceback
from typing import List

import disnake
from disnake.ext import tasks, commands

import keep_alive
from logger import logger
from models.users.discord import DCUser, dc_users
from models.users.valorant import (
    ValStats,
    ValUser,
    fullname2puuid,
    val_users,
    val_user_stats,
)
from settings import settings
from utils import get_rank_order

"""
For bot developers:

features proposed:


features in progress:


features finished:

"""

intents = disnake.Intents.all()
command_sync_flags = commands.CommandSyncFlags.all()

bot = commands.Bot(
    command_prefix="!",
    command_sync_flags=command_sync_flags,
    intents=intents,
    test_guilds=[settings.test_server_id],
    help_command=None,
    activity=disnake.Activity(
        name=f"{len(val_users)} users stats", type=disnake.ActivityType.watching
    ),
)


@bot.event
async def on_ready() -> None:
    logger.info("We have logged in as {0.user}".format(bot))
    update.start()


@bot.slash_command()
async def hello(inter: disnake.ApplicationCommandInteraction) -> None:
    """
    Responds with 'Hello World'. Used for testing.
    """
    await inter.response.defer()
    await inter.edit_original_response(f"Hello World! {inter.author.mention}")


@bot.slash_command()
async def help(inter: disnake.ApplicationCommandInteraction, command: str = "") -> None:
    """
    Print information for commands

    Parameters
    ----------
    command: (Optional) The command you want to view the detailed help message.
    """
    await inter.response.defer()
    embed = disnake.Embed(title="Commands Info", color=disnake.Color.blue())
    if command != "":
        for s_command in bot.slash_commands:
            if s_command.name == command:
                val = s_command.description
                for option in s_command.options:
                    val += "\n"
                    val += option.name + " - " + option.description
                embed.add_field(name=command, value=val, inline=True)
                await inter.edit_original_response(embed=embed)
                return
        embed.description = f"Command {command} doesn't exist."
    else:
        for s_command in bot.slash_commands:
            embed.add_field(
                name=s_command.name, value=s_command.description, inline=True
            )
    await inter.edit_original_response(embed=embed)


@bot.slash_command(name="all_stats", description="Get all users' stats.")
async def all_stats(inter: disnake.ApplicationCommandInteraction) -> None:
    """
    Get all users' stats.
    """
    await inter.response.defer()
    embed = disnake.Embed(
        title="Stats of All Registered Users", color=disnake.Color.blue()
    )
    for key in sorted(val_users.keys(), key=lambda x: x.lower()):
        val_user: ValUser = val_users[key]
        val = f"Highest rank: {val_user.hrank}\nCurrent rank: {val_user.crank}\nElo: {val_user.elo}"
        embed.add_field(name=val_user.fullname, value=val, inline=True)
    await inter.edit_original_response(embed=embed)


@bot.slash_command(name="stats")
async def stats(
    inter: disnake.ApplicationCommandInteraction,
    member: disnake.User | disnake.Member | None = None,
    count: int = 5,
) -> None:
    """
    Get user's stats.

    Parameters
    ----------
    member: The id of the discord user.
    """
    await inter.response.defer()
    if member is None:
        member = inter.author
    user: ValUser = dc_users[member.id].val_user
    stats: List[ValStats] = dc_users[member.id].val_user_stats
    logger.info(user)
    embed = disnake.Embed(title=f"Stats of @{member} ", color=disnake.Color.blue())
    embed.add_field(name="Highest rank", value=user.hrank, inline=True)
    embed.add_field(name="Current rank", value=user.crank, inline=True)
    embed.add_field(name="Elo", value=user.elo, inline=True)
    embed.set_footer(
        text=user.fullname,
        icon_url=(
            user.crank_img if hasattr(user, "crank_img") and user.crank_img else None
        ),
    )

    if stats:
        recent_c_performance = "`❔ W-L  Agent    ADR  K/ D/ A HS d`\n"
        for valstats in stats[: min(50, count)]:
            kda = f"{valstats.kills: >2}/{valstats.deaths: >2}/{valstats.assists: >2}"
            line = (
                f"`{valstats.result}{valstats.wins: >2}-{valstats.loses: <2} "
                + f"{valstats.agent: <8} {valstats.damage: >3} {kda: <8} "
                + f"{min(99, valstats.headshot): >2} "
                + f"{min(round((datetime.utcnow()-valstats.time).total_seconds() / 60 / 60 / 24), 9): >1}`\n"
            )
            tmp = recent_c_performance + line
            if len(tmp) > 1000:
                break
            recent_c_performance = tmp
        embed.add_field(
            name="Recent Competitive Performance", value=recent_c_performance
        )
    await inter.edit_original_response(embed=embed)


@bot.slash_command(name="expire")
async def expire(inter: disnake.ApplicationCommandInteraction) -> None:
    """
    Force expire user's stats.
    """
    await inter.response.defer()
    val_users.expire(dc_users[inter.author.id].val_id)
    await inter.edit_original_response("expire done")


@bot.slash_command(name="all_expire")
async def all_val_expire(inter: disnake.ApplicationCommandInteraction) -> None:
    """
    Force expire all user's stats.
    """
    await inter.response.defer()
    for key in val_users.keys():
        val_users.expire(key)
    await inter.edit_original_response("expire done")


@bot.slash_command(name="all_delete")
@commands.default_member_permissions(administrator=True)
async def all_delete(inter: disnake.ApplicationCommandInteraction) -> None:
    """
    Delete all users from the user list of this server (admin only).
    """
    await inter.response.defer()
    for fullname in val_users.keys():
        val_users.pop(fullname)
    await inter.edit_original_response("Successfully deleted all users from user list!")


@bot.slash_command(name="review")
async def review(
    inter: disnake.ApplicationCommandInteraction,
    game: str = commands.Param(choices=["apex", "valorant"]),
) -> None:
    """
    Give a fair and objective review of a game.

    Parameters
    ----------
    game: The game you want to review.
    """
    await inter.response.defer()
    game_description = ""
    if game == "apex":
        game_description = "Apex legends has been a trash game ever since I first played it in 2019.. the players are toxic, the map is shit, like it’s not cool or interesting to me, the guns do fuck all for damage and everything is all over the place to find.. and yeah the servers and controller aim assist do suck. After all, the current season is garbage."
    elif game == "valorant":
        game_description = "VALORANT is a character-based 5v5 tactical shooter set on the global stage. Outwit, outplay, and outshine your competition with tactical abilities, precise gunplay, and adaptive teamwork. CREATIVITY IS YOUR GREATEST WEAPON!"

    embed = disnake.Embed(
        title=f"Fair and Objective Review of {game}",
        description=game_description,
        color=disnake.Color.blue(),
    )
    await inter.edit_original_response(embed=embed)


@bot.slash_command(name="crank")
async def crank(inter: disnake.ApplicationCommandInteraction, limit: int = 0) -> None:
    """
    Print users who have highest current rank in the user list.

    Parameters
    ----------
    limit: An integer value that represent how many users you want to print.
    """
    await inter.response.defer()
    userList, rankList = get_rank_order(val_users, "crank", limit)
    embed = disnake.Embed(title="Current Ranks", color=disnake.Color.blue())
    embed.add_field(name="Val User", value="\n".join(userList), inline=True)
    embed.add_field(name="Rank", value="\n".join(rankList), inline=True)
    await inter.edit_original_response(embed=embed)


@bot.slash_command(name="hrank")
async def hrank(inter: disnake.ApplicationCommandInteraction, limit: int = 0) -> None:
    """
    Print users who have highest lifetime rank in the user list.

    Parameters
    ----------
    limit: An integer value that represent how many users you want to print.
    """
    await inter.response.defer()
    userList, rankList = get_rank_order(val_users, "hrank", limit)
    embed = disnake.Embed(title="Highest Ranks", color=disnake.Color.blue())
    embed.add_field(name="Val User", value="\n".join(userList), inline=True)
    embed.add_field(name="Rank", value="\n".join(rankList), inline=True)
    await inter.edit_original_response(embed=embed)


@bot.slash_command(name="bind_val")
async def bind_val(
    inter: disnake.ApplicationCommandInteraction,
    fullname: str,
    member: disnake.User | disnake.Member | None = None,
) -> None:
    """
    Bind a Valorant user to a discord user and add it to the user list.

    Parameters
    ----------
    fullname: The valorant user fullname, should be in the form <valorant_name>#<valorant_tag>
    member: The id of the discord user. If none, then by default bind to who execute this command.
    """
    await inter.response.defer()
    if member is None:
        member = inter.author
    dc_user = dc_users[member.id] if member.id in dc_users else DCUser()
    puuid = fullname2puuid(fullname)
    dc_user.val_id = puuid
    dc_users[member.id] = dc_user
    _ = val_users[puuid]  # write to val_users
    _ = val_user_stats[puuid]  # write to val_user_stats
    await inter.edit_original_response(f"Done!")
    await bot.change_presence(
        status=bot.status,
        activity=disnake.Activity(
            name=f"{len(val_users)} users stats", type=disnake.ActivityType.watching
        ),
    )


EMOJIS = [
    "0️⃣",
    "1️⃣",
    "2️⃣",
    "3️⃣",
    "4️⃣",
    "5️⃣",
    "6️⃣",
    "7️⃣",
    "8️⃣",
    "9️⃣",
    "🇦",
    "🇧",
]


@bot.slash_command(name="vote")
async def vote(
    inter: disnake.ApplicationCommandInteraction,
    title: str = "Vote",
    interval_min: int = 60,
    count: int = 12,
) -> None:
    count = min(count, 12)
    await inter.response.defer()
    embed = disnake.Embed(title=title, color=disnake.Color.blue())
    now = int(time.time())
    for i, reaction in enumerate(EMOJIS[:count]):
        embed.add_field(
            name=f"{reaction}: <t:{now + (i+1) * 60 * interval_min}:R>",
            value=0,
            inline=True,
        )
    msg = await inter.original_message()
    await asyncio.gather(
        inter.edit_original_response(embed=embed),
        *[msg.add_reaction(emoji) for emoji in EMOJIS],
    )


async def on_reaction_change(
    reaction: disnake.Reaction, user: disnake.User | disnake.Member
):
    msg = reaction.message
    if msg.author.id != bot.user.id or user.id == bot.user.id:
        return
    if reaction.emoji not in EMOJIS or not msg.embeds or msg.embeds[0].title != "Vote":
        return
    embed = msg.embeds[0]
    i = EMOJIS.index(reaction.emoji)
    embed.set_field_at(i, embed.fields[i].name, reaction.count - 1)
    await msg.edit(embed=embed)


@bot.event
async def on_reaction_add(
    reaction: disnake.Reaction, user: disnake.User | disnake.Member
):
    await on_reaction_change(reaction, user)


@bot.event
async def on_reaction_remove(
    reaction: disnake.Reaction, user: disnake.User | disnake.Member
):
    await on_reaction_change(reaction, user)


@bot.event
async def on_slash_command_error(
    inter: disnake.ApplicationCommandInteraction, exception: commands.CommandError
):
    logger.error(
        f"An exception occurred: {exception}"
        + "\n".join(
            traceback.format_exception(
                type(exception), exception, exception.__traceback__
            )
        )
    )
    await inter.edit_original_response(f"{exception}! Please contact the developer!")


@tasks.loop(seconds=10.0)
async def update() -> None:
    """
    Update dataset automatically in the background.
    """
    for key, value in val_users.items():
        val_users.expire(key)
        val_user_stats.expire(key)
        logger.info(f"Stats of {value.fullname} updated at {time.time() - val_users.last_fetch_time[key]}s ago.")
        break


if __name__ == "__main__":
    if settings.is_repl_it:
        keep_alive.keep_alive()
    bot.run(settings.token)
