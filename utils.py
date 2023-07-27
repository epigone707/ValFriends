import requests
from sqlitedict import SqliteDict
from settings import settings

users = SqliteDict(settings.db_filename, tablename="users", autocommit=True)


def update_user_stats(fullname):
  """
  send GET request to get the most up-to-date stats of a user
  update users
  return the user stats as a dict
  """
  name, tag = fullname.split("#")
  response = requests.get(
    f"https://api.henrikdev.xyz/valorant/v2/mmr/na/{name}/{tag}")
  json_data = response.json()
  if json_data["status"] != 200:
    print("error code: ", json_data["status"])
    return None
  profile = {
    "hrank": json_data['data']['highest_rank']['patched_tier'],
    "crank": json_data['data']['current_data']['currenttierpatched'],
    "elo": json_data['data']['current_data']['elo'],
  }
  users[fullname] = profile
  return profile


def get_user_stats(fullname):
  """
  get stats for a user from the cached file users
  """
  if fullname not in users:
    # cache miss
    return update_user_stats(fullname)

  return users[fullname]


def add_user(fullname):
  return update_user_stats(fullname)


def delete_user(fullname):
  users.pop(fullname)


def get_users():
  return dict(users)
