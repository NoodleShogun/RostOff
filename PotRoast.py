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
              "Yo mama so fat she occupies Wall St by herself!",
              "I took a picture of your mom, got it developed. When I hung it up, the nail bent.",
              "You’re so poor, your house is so small, when you order a pizza you have to eat it outside.",
              "I'm trying my absolute hardest to see things from your perspective, "
              "but I can't get my head that far up my ass.",
              "Some day you’ll go far—and I really hope you stay there.",
              "Sometimes it’s better to keep your mouth shut and give the impression "
              "that you’re stupid than open it and remove all doubt.",
              "I don’t know what your problem is, but I’m guessing it’s hard to pronounce.",
              "Do your parents even realize they’re living proof that two wrongs don’t make a right?",
              "Remember that time I said I thought you were cool? I lied.",
              "Can you die of constipation? I ask because I’m worried about how full of shit you are."]

    roasts2 = ["To find the amount of Friends you have you must firs take the required amount of parameters "
               "you put in divided by the amount needed."]

    if not user:
        await client.say(""+random.choice(roasts2), tts=True)
    else:
        await client.say(""+ user.mention + " " + random.choice(roasts), tts=True)


# Core Functions

# core commands

client.run(TOKEN)
