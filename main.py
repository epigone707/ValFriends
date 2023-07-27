import os
import keep_alive
import disnake
from disnake.ext import commands

from utils import get_user_stats, add_user, delete_user, get_users

intents = disnake.Intents.default()
intents.message_content = True
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

bot = commands.Bot(command_prefix='!',
                   command_sync_flags=command_sync_flags,
                   intents=intents)

# """
# For bot developers:

# features proposed:
# - get user's recent kda
# - get user's recent winrate
# - update the userlist cache (users.json) in some way. option1: add a timestamp for every user in the cache. option2: add an option in stats command or add a new command to update the cache
# - add rank icon to every rank shown in stats, allstats and crank. There is a icon url in the return json from API, just store it in the cache!

# features in progress:
# - use command tree sync() to let our commands show in user input box

# features finished:
# -

# """

# @client.event
# async def on_ready():
#   print("Bot is ready!")
#   try:
#     # Add the guild id in which the slash command will appear.
#     # If it should be in all, remove the argument,
#     # but note that it will take some time (up to an hour) to register the command if it's for all guilds
#     synced = await tree.sync(guild=discord.Object(id=SERVER_ID))
#     print(f"Synced {len(synced)} commmand(s)")
#   except Exception as e:
#     print(e)
#   print('We have logged in as {0.user}'.format(client))

# @tree.command(name="commandname",
#               description="My first application Command",
#               guild=discord.Object(id=SERVER_ID))
# async def first_command(interaction):
#   await interaction.response.send_message("My first application Command!")


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))


@bot.slash_command(description="Responds with 'World'")
async def hello(inter):
  await inter.response.send_message("World")


@bot.slash_command(description="Get all users' stats.")
async def allstats(inter):
  users = get_users()
  embed = disnake.Embed(title="Stats of All Registered Users",
                        color=disnake.Color.blue())
  for user, profile in users.items():
    val = f"Highest rank: {profile['hrank']}\nCurrent rank: {profile['crank']}\nElo: {str(profile['elo'])}"
    embed.add_field(name=user, value=val, inline=True)
  await inter.response.send_message(embed=embed)


@bot.slash_command(name="stats",
                   description="Get user's stats. usage: <username>#<tag>.")
async def stats(inter, fullname: str):
  res = get_user_stats(fullname)
  embed = disnake.Embed(title=f"Stats of {fullname}",
                        color=disnake.Color.blue())
  embed.add_field(name='Highest rank', value=res["hrank"], inline=True)
  embed.add_field(name='Current rank', value=res["crank"], inline=True)
  embed.add_field(name='Elo', value=res["elo"], inline=True)
  await inter.response.send_message(embed=embed)


@bot.slash_command(
  name='add',
  description=
  "Add a user to the user list of this server. usage: <username>#<tag>")
async def add(inter, fullname: str = ""):
  if fullname == "":
    await inter.response.send_message(
      'Error: Please enter your username and tag')
  resMsg = f"Sucessfully added {fullname} to user list!"
  if add_user(fullname) == None:
    resMsg = f"Failed to add {fullname} to user list!"
  await inter.response.send_message(resMsg)


@bot.slash_command(
  name='delete',
  description=
  "Delete a user from the user list of this server. usage: /delete <username>#<tag>"
)
async def delete(inter, fullname: str = ""):
  if fullname == "":
    await inter.response.send_message(
      'Error: Please enter your username and tag')
  delete_user(fullname)
  await inter.response.send_message(
    f"Sucessfully deleted {fullname} from user list!")


@bot.slash_command(name='userlist', description="Print user list.")
async def userlist(inter):
  users = get_users()
  embed = disnake.Embed(title="All Valorant Users Registered In This Server",
                        color=disnake.Color.blue())
  embed.add_field(name='Users', value="\n".join(users.keys()), inline=True)
  await inter.response.send_message(embed=embed)


@bot.slash_command(
  name='apex',
  description="Give a fair and objective review of the game APEX.")
async def apex(inter):
  embed = disnake.Embed(
    title="Fair and Objective Review of APEX",
    description=
    "Alex legends has been a trash game ever since I first played it in 2019.. the players are toxic, the map is shit, like it’s not cool or interesting to me, the guns do fuck all for damage and everything is all over the place to find.. and yeah the servers do suck. After all, the current season is garbage.",
    color=disnake.Color.blue())
  await inter.response.send_message(embed=embed)


@bot.slash_command(
  name='valorant',
  description="Give a fair and objective review of the game VALORANT.")
async def valorant(inter):
  embed = disnake.Embed(
    title="Fair and Objective Review of VALORANT",
    description=
    "VALORANT is a character-based 5v5 tactical shooter set on the global stage. Outwit, outplay, and outshine your competition with tactical abilities, precise gunplay, and adaptive teamwork. CREATIVITY IS YOUR GREATEST WEAPON!",
    color=disnake.Color.blue())
  await inter.response.send_message(embed=embed)


@bot.slash_command(
  name='crank',
  description=
  "Print users who have highest current rank in the user list. usage: /crank [optional_num]"
)
async def crank(inter, limit: str = "0"):
  if limit:
    limit = int(limit)
  users = get_users()

  def compare_crank(username):
    ranks = [
      "Iron", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ascendant",
      "Immortal", "Radiant"
    ]
    crank = users[username]["crank"]
    if crank is None:
      return 0
    rank, level = crank.split(" ")
    return ranks.index(rank) * 10 + int(level)

  users = list(users.keys())
  users.sort(key=compare_crank, reverse=True)
  if limit > 0:
    users = users[:limit]
  embed = disnake.Embed(title="Current Ranks", color=disnake.Color.blue())
  embed.add_field(name='Val User', value='\n'.join(users), inline=True)
  embed.add_field(name='Rank',
                  value='\n'.join(
                    map(lambda x: users[x]["crank"] or "Unranked", users)),
                  inline=True)
  await inter.response.send_message(embed=embed)


if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(os.getenv("TOKEN"))
