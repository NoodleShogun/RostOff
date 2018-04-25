# https://github.com/NoodleShogun/RostOff/tree/master

# imports
from discord.ext.commands import Bot
import discord

from discord import Game
import asyncio
import aiohttp
import random

# bot prefixes
BOT_PREFIX = ("!")

# variables and other stuff

TOKEN = 'NDM4MDgyMTAyOTUzNzcxMDEw.Db_buQ._9gFilYm4oRyurUMPACaJ4DrLxs'
client = Bot(command_prefix=BOT_PREFIX)

# Command Functions


@client.command(name="roast")
async def roast(user: discord.User=None):
    roasts = ["If I wanted to Commit Suicide I'd climb your Ego and Jump to your IQ.", "Ur Mom Gay",
              "One might say that you lack an ability to process reasonable explanations for sticky situations.",
              "Yo mama so fat she occupies Wall St by herself!"
              ]

    if not user:
        await client.say(""+random.choice(roasts))
    else:
        await client.say(""+ user.mention + " " + random.choice(roasts))


# Core Functions

# core commands

client.run(TOKEN)
