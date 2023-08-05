# ValFriends
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge)](#)
[![disnake 2.9.0+](https://img.shields.io/badge/disnake-2.9.0+-blue.svg?style=for-the-badge)](#)

A Discord bot for game Valorant, aims for helping you play with your friends happily.

Just need a simple command to register your valorant account into the user list. You can easily view stats and rank info for everyone in the discord server.


## Installation

Install [Poetry](https://python-poetry.org/) first.

Run once for installing dependencies:
```
poetry install --with dev
```

Enter poetry shell and run:
```
poetry shell
python3 main.py
```

You need to set environment variables `TEST_SERVER_ID`(your discord server id, so that when you add new commands to this bot they can be loaded faster) and `TOKEN`(your discord bot token) by creating an `.env` file. You can refer to `.env.example`.

We provides `keep_alive.py` in case you want to host the bot on [replit](https://replit.com/~).

## Basic Usage

### Step 1: Bind a Valorant account to a Discord account
Originally, the user list is empty. You can bind your valorant account with your discord account to the user list by executing:
```
/bind_val <valorant_name>#<valorant_tag>
```
![image](https://github.com/epigone707/ValFriends/assets/62321106/5b40c82d-7b3c-4aee-bbd0-0f3409ebfea9)

Or you can help your friends bind their accounts:
```
/bind_val <friend_valorant_name>#<friend_valorant_tag> <friend_discord_name>
```

### Step 2: Play with all commands!
To show your stats, execute:
```
/stats
```
![image](https://github.com/epigone707/ValFriends/assets/62321106/2e83303d-9be5-4d7c-b46f-7c8b61a7096f)

To show your friend's stats, execute:
```
/stats <friend_discord_name>
```


When you execute commands that require discord id as input, it will autocomplete based on your input:
![auto](https://github.com/epigone707/ValFriends/assets/62321106/3ffbddc7-6312-45bf-8dbd-568d2a7e36ce)



To print users in sorted order of current rank, use `/crank`.

To print users in sorted order of lifetime highest rank, use `/hrank`.

To print stats for all users, use `/all_stats`

Note that the profile for every user in the user list is cached in a sqlite database. When you execute `stats`, the bot actually returns the data in cache.

The bot generates a timestamp for every profile. The profile will expire after some time and the bot will fetched the up-to-date data from the API.

You can also force the cache to update by using `/expire` or `/all_expire`.





## All Commands
Execute `/help` to get the help message for all supported commands:
```
all_stats   - Get all users' stats.
stats       - Get user's stats.
crank       - Print users who have highest current rank in the user list.
all_expire  - Force expire all user's stats.
hrank       - Print users who have highest lifetime rank in the user list.
expire      - Force expire user's stats.
help        - Print information for commands
review      - Give a fair and objective review of a game.
bind_val    - Bind a Valorant user to a discord user and add it to the user list.
all_delete  - Delete all users from the user list of this server (admin only).
hello       - Responds with 'Hello World'. Used for testing.
```
You can also execute `help <command>` to view the details of the command parameters.


## API reference
A big thank you to [Henrik](https://github.com/Henrik-3/unofficial-valorant-api)!

## Contributors
- [@BoYanZh](https://github.com/BoYanZh)
- [@Yijie-Shi0829](https://github.com/Yijie-Shi0829)
- Me!
