import discord
import os
import valorant
import json
import requests

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def update_user_stats(name, tag):
  """
  send GET request to get the most up-to-date stats of a user
  update users.json
  return the user stats as a dict
  """
  response = requests.get(
    f"https://api.henrikdev.xyz/valorant/v2/mmr/na/{name}/{tag}")
  json_data = json.loads(response.text)
  if json_data["status"] != 200:
    print("error code: ", json_data["status"])
    return None
  with open('users.json') as f:
    cached_data = json.load(f)
  fullname = f"{name}#{tag}"
  profile = {
    "hrank": json_data['data']['highest_rank']['patched_tier'],
    "crank": json_data['data']['current_data']['currenttierpatched'],
    "elo": json_data['data']['current_data']['elo'],
  }
  cached_data["userList"][fullname] = profile
  with open("users.json", "w") as outfile:
    outfile.write(json.dumps(cached_data))
  return profile


def get_user_stats(name, tag):
  """
  get stats for a user from the cached file users.json
  """
  with open('users.json') as f:
    data = json.load(f)
  fullname = f"{name}#{tag}"

  if fullname not in data["userList"]:
    # cache miss
    return update_user_stats(name, tag)

  return data["userList"][fullname]


def add_user(name, tag):
  return update_user_stats(name, tag)


def read_users():
  with open('users.json') as f:
    data = json.load(f)
  return data


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content

  if msg.startswith('/hello'):
    await message.channel.send('Hello!')

  # if msg.startswith('/leader'):
  #   lb = riot_client.get_leaderboard(size=15)
  #   res = "Top Players in NA:\n"
  #   for p in lb.players:
  #     res += f"#{p.leaderboardRank} - {p.gameName} ({p.numberOfWins} wins)\n"
  #   await message.channel.send(res)

  if msg.startswith('/stats'):
    sp = msg.split(" ")
    name = sp[1]
    tag = sp[2]
    res = get_user_stats(name, tag)
    embed = discord.Embed(title=f"Stats of {name}#{tag}",
                          color=discord.Color.blue())
    embed.add_field(name='Highest rank', value=res["hrank"], inline=True)
    embed.add_field(name='Current rank', value=res["crank"], inline=True)
    embed.add_field(name='Elo', value=res["elo"], inline=True)
    await message.channel.send(embed=embed)

  if msg.startswith('/allstats'):
    data = read_users()
    embed = discord.Embed(title="Stats of All Registered Users",
                          color=discord.Color.blue())
    for user, profile in data["userList"].items():
      sp = user.split("#")
      name, tag = sp[0], sp[1]
      val = f"Highest rank: {profile['hrank']}\nCurrent rank: {profile['crank']}\nElo: {str(profile['elo'])}"
      embed.add_field(name=user, value=val, inline=True)

    await message.channel.send(embed=embed)

  if msg.startswith('/add'):
    sp = msg.split(" ")
    name, tag = sp[1], sp[2]
    if add_user(name, tag) == None:
      await message.channel.send(f"Failed to add {name}#{tag} to user list!")
    else:
      await message.channel.send(f"Sucessfully added {name}#{tag} to user list!")

  if msg.startswith('/userlist'):
    data = read_users()
    embed = discord.Embed(title="All Valorant Users Registered In This Server",
                          color=discord.Color.blue())
    embed.add_field(name='Users',
                    value="\n".join(data["userList"].keys()),
                    inline=True)
    await message.channel.send(embed=embed)


client.run(os.getenv('TOKEN'))
