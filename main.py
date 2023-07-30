import disnake
from disnake.ext import commands

import keep_alive
from logger import logger
from models.users import users
from settings import settings
from utils import get_rank_order

"""
For bot developers:

features proposed:
- add rank icon to every rank shown in stats, allstats and crank. There is a icon url in the return json from API, just store it in the cache!

features in progress:


features finished:
- update the userlist cache in some way. option1: add a timestamp for every user in the cache. option2: add an option in stats command or add a new command to update the cache
- use slash commands to let them show when user types '/'
- support help slash command. Need to show the info for each parameter when user clicks on it.
- get user's recent matches stats like kda
- autocomplete username

"""

intents = disnake.Intents.default()
intents.message_content = True
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

bot = commands.Bot(command_prefix='!',
                   command_sync_flags=command_sync_flags,
                   intents=intents,
                   test_guilds=[settings.test_server_id],
                   help_command=None)


@bot.event
async def on_ready():
  logger.info('We have logged in as {0.user}'.format(bot))


@bot.slash_command()
async def hello(inter: disnake.ApplicationCommandInteraction):
  """
  Responds with 'Hello World'. Used for testing.
  """
  await inter.response.send_message(f"Hello World! {inter.author.mention}")


@bot.slash_command()
async def help(inter: disnake.ApplicationCommandInteraction, command=""):
  """
  Print information for commands
  
  Parameters
  ----------
  command: (Optional) The command you want to view the detailed help message.
  """
  embed = disnake.Embed(title="Commands Info", color=disnake.Color.blue())
  if command != "":
    for s_command in bot.slash_commands:
      if s_command.name == command:
        val = s_command.description
        for option in s_command.options:
          val += '\n'
          val += option.name + ' - ' + option.description
        embed.add_field(name=command, value=val, inline=True)
        await inter.response.send_message(embed=embed)
        return
    embed.description = f"Command {command} doesn't exist."
  else:
    for s_command in bot.slash_commands:
      embed.add_field(name=s_command.name,
                      value=s_command.description,
                      inline=True)
  await inter.response.send_message(embed=embed)


@bot.slash_command(description="Get all users' stats.")
async def allstats(inter: disnake.ApplicationCommandInteraction):
  """
  Get all users' stats.
  """
  embed = disnake.Embed(title="Stats of All Registered Users",
                        color=disnake.Color.blue())
  for user in sorted(users.keys(), key=lambda x: x.lower()):
    profile = users[user]
    val = f"Highest rank: {profile.hrank}\nCurrent rank: {profile.crank}\nElo: {profile.elo}"
    embed.add_field(name=user, value=val, inline=True)
  await inter.response.send_message(embed=embed)


async def autocomp_username(inter: disnake.ApplicationCommandInteraction, user_input: str):
    return [user for user in users if user_input.lower() in user.lower()]

@bot.slash_command(name="stats")
async def stats(inter: disnake.ApplicationCommandInteraction, fullname: str = commands.Param(autocomplete=autocomp_username)):
  """
  Get user's stats.
  
  Parameters
  ----------
  fullname: The fullname of the player, should be in the form: <username>#<tag>.
  """
  res = users[fullname]
  logger.info(fullname)
  logger.info(res)
  embed = disnake.Embed(title=f"Stats of {res.fullname}",
                        color=disnake.Color.blue())
  embed.add_field(name='Highest rank', value=res.hrank, inline=True)
  embed.add_field(name='Current rank', value=res.crank, inline=True)
  embed.add_field(name='Elo', value=res.elo, inline=True)

  if res.recent_stats:
    recent_c_performance = ""
    for valstats in res.recent_stats:
      kda = f"kda:{valstats.kills}/{valstats.deaths}/{valstats.assists}"
      recent_c_performance += f"{valstats.result}  dmg:{valstats.damage} {kda}\n"
    embed.add_field(name='Recent Competitive Performance',
                    value=recent_c_performance,
                    inline=True)
  await inter.response.send_message(embed=embed)


@bot.slash_command(name="expire")
async def expire(inter: disnake.ApplicationCommandInteraction, fullname: str = commands.Param(autocomplete=autocomp_username)):
  """
  Force expire user's stats.
  
  Parameters
  ----------
  fullname: The fullname of the player, should be in the form: <username>#<tag>.
  """
  await inter.response.send_message('expire started')
  users.expire(fullname)


@bot.slash_command(name="allexpire")
async def allexpire(inter: disnake.ApplicationCommandInteraction):
  """
  Force expire all user's stats.
  """
  await inter.response.send_message('expire started')
  for fullname in users.keys():
    users.expire(fullname)


@bot.slash_command(name='delete')
@commands.default_member_permissions(administrator=True)
async def delete(inter: disnake.ApplicationCommandInteraction, fullname: str = commands.Param(autocomplete=autocomp_username)):
  """
  Delete a user from the user list of this server (admin only).
  
  Parameters
  ----------
  fullname: The fullname of the player, should be in the form: <username>#<tag>.
  """
  users.pop(fullname)
  await inter.response.send_message(
    f"Successfully deleted {fullname} from user list!")


@bot.slash_command(name='alldelete')
@commands.default_member_permissions(administrator=True)
async def alldelete(inter: disnake.ApplicationCommandInteraction):
  """
  Delete all users from the user list of this server (admin only).
  """
  for fullname in users.keys():
    users.pop(fullname)
  await inter.response.send_message(
    "Successfully deleted all users from user list!")


@bot.slash_command(name='userlist')
async def userlist(inter: disnake.ApplicationCommandInteraction):
  """
  Print user list.
  """
  embed = disnake.Embed(title="All Valorant Users Registered In This Server",
                        color=disnake.Color.blue())
  embed.add_field(name='Users',
                  value="\n".join(sorted(users.keys(),
                                         key=lambda x: x.lower())),
                  inline=True)
  await inter.response.send_message(embed=embed)


@bot.slash_command(name='review')
async def review(inter: disnake.ApplicationCommandInteraction,
                 game: str = commands.Param(choices=["apex", "valorant"])):
  """
  Give a fair and objective review of a game.
  
  Parameters
  ----------
  game: The game you want to review.
  """
  game_description = ""
  if game == "apex":
    game_description = "Apex legends has been a trash game ever since I first played it in 2019.. the players are toxic, the map is shit, like it’s not cool or interesting to me, the guns do fuck all for damage and everything is all over the place to find.. and yeah the servers and controller aim assist do suck. After all, the current season is garbage."
  elif game == "valorant":
    game_description = "VALORANT is a character-based 5v5 tactical shooter set on the global stage. Outwit, outplay, and outshine your competition with tactical abilities, precise gunplay, and adaptive teamwork. CREATIVITY IS YOUR GREATEST WEAPON!"

  embed = disnake.Embed(title=f"Fair and Objective Review of {game}",
                        description=game_description,
                        color=disnake.Color.blue())
  await inter.response.send_message(embed=embed)


@bot.slash_command(name='crank')
async def crank(inter: disnake.ApplicationCommandInteraction, limit: int = 0):
  """
  Print users who have highest current rank in the user list.
  
  Parameters
  ----------
  limit: An integer value that represent how many users you want to print.
  """
  userList, rankList = get_rank_order(users, "crank", limit)
  embed = disnake.Embed(title="Current Ranks", color=disnake.Color.blue())
  embed.add_field(name='Val User', value='\n'.join(userList), inline=True)
  embed.add_field(name='Rank', value='\n'.join(rankList), inline=True)
  await inter.response.send_message(embed=embed)


@bot.slash_command(name='hrank')
async def hrank(inter: disnake.ApplicationCommandInteraction, limit: int = 0):
  """
  Print users who have highest lifetime rank in the user list.
  
  Parameters
  ----------
  limit: An integer value that represent how many users you want to print.
  """
  userList, rankList = get_rank_order(users, "hrank", limit)
  embed = disnake.Embed(title="Highest Ranks", color=disnake.Color.blue())
  embed.add_field(name='Val User', value='\n'.join(userList), inline=True)
  embed.add_field(name='Rank', value='\n'.join(rankList), inline=True)
  await inter.response.send_message(embed=embed)


if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(settings.token)
