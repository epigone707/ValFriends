import disnake
from disnake.ext import commands

import keep_alive
from logger import logger
from models.users.discord import DCUser, dc_users
from models.users.valorant import ValUser, fullname2puuid, val_users
from settings import settings
from utils import get_rank_order

"""
For bot developers:

features proposed:


features in progress:


features finished:
- update the userlist cache in some way. option1: add a timestamp for every user in the cache. option2: add an option in stats command or add a new command to update the cache
- use slash commands to let them show when user types '/'
- support help slash command. Need to show the info for each parameter when user clicks on it.
- get user's recent matches stats like kda
- autocomplete username
- add rank icon to every rank shown in stats, all_stats and crank. There is a icon url in the return json from API, just store it in the cache!

"""

intents = disnake.Intents.default()
intents.message_content = True
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

bot = commands.Bot(
    command_prefix="!",
    command_sync_flags=command_sync_flags,
    intents=intents,
    test_guilds=[settings.test_server_id],
    help_command=None,
)


@bot.event
async def on_ready() -> None:
    logger.info("We have logged in as {0.user}".format(bot))


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
) -> None:
    """
    Get user's stats.

    Parameters
    ----------
    fullname: The fullname of the player, should be in the form: <username>#<tag>.
    """
    await inter.response.defer()
    if member is None:
        member = inter.author
    res: ValUser = dc_users[member.id].val_user
    logger.info(res)
    embed = disnake.Embed(title=f"Stats of {res.fullname}", color=disnake.Color.blue())
    embed.add_field(name="Highest rank", value=res.hrank, inline=True)
    embed.add_field(name="Current rank", value=res.crank, inline=True)
    embed.add_field(name="Elo", value=res.elo, inline=True)
    if hasattr(res, "crank_img") and res.crank_img:
        embed.set_thumbnail(url=res.crank_img)

    if res.recent_stats:
        recent_c_performance = ""
        for valstats in res.recent_stats:
            kda = f"kda:{valstats.kills}/{valstats.deaths}/{valstats.assists}"
            recent_c_performance += (
                f"{valstats.result} {valstats.agent} dmg:{valstats.damage} {kda}\n"
            )
        embed.add_field(
            name="Recent Competitive Performance",
            value=recent_c_performance,
            inline=True,
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
    await inter.response.defer()
    if member is None:
        member = inter.author
    dc_user = dc_users[member.id] if member.id in dc_users else DCUser()
    puuid = fullname2puuid(fullname)
    dc_user.val_id = puuid
    dc_users[member.id] = dc_user
    _ = val_users[puuid]  # write to val_users
    await inter.edit_original_response(f"Done!")


if __name__ == "__main__":
    if settings.is_repl_it:
        keep_alive.keep_alive()
    bot.run(settings.token)
