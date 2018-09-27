# https://github.com/NoodleShogun/RostOff/tree/master

# imports
import os, discord, random, markovify
from discord.ext.commands import Bot

is_prod = os.environ.get('IS_HEROKU', None)

if is_prod:
    BOT_PREFIX = os.environ['prefix']
    TOKEN = os.environ['token']
else:
    BOT_PREFIX = os.environ['prefix']
    TOKEN = os.environ['token']

client = Bot(command_prefix=BOT_PREFIX)
canTTS = True


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Dark Souls III"))


@client.event
async def on_member_join(member):
    with open("data/roasts.txt") as f:
        roasts = f.readlines()

    channel_id = 427040067119349760

    if channel_id is None:

        channel_id = 434894895921102859
    else:

        channel_id = 356280580012376075

    await client.say(discord.Object(id=channel_id),  member.mention + " " + random.choice(roasts))


@client.command(name="pizza")
async def pizza_time():
    await client.say("Pizza time! " + ":pizza:")


@client.command(name="tts")
async def entts(enable=False):

        global canTTS
        if enable:
            print("TTS set to TRUE")
            canTTS = True
        else:
            print("TTS set to FALSE")
            canTTS = False


@client.command(name="roast")
async def roast(user: discord.User=None):
    with open("data/roasts.txt") as f:
        roasts = f.readlines()

        roasts2 = ["To find the amount of Friends you have you must first take the required amount of parameters "
                   "you put in divided by the amount needed."]

    if not user:
        await client.say(""+random.choice(roasts2), tts=canTTS)
    else:
        await client.say(""+ user.mention + " " + random.choice(roasts), tts=canTTS)


@client.command(name="conspiracy")
async def conspiracy():
    with open("data/conspiracy.txt") as f:
        text = f.read()
    text_model = markovify.Text(text)
    for i in range(1):
        nonsense = text_model.make_sentence()
        await client.say(""+nonsense)


@client.command(name="makeRoast")
async def make_roast():
    with open("data/roasts.txt") as r:
        text = r.read()
    text_model = markovify.Text(text)
    for i in range(1):
        nonsense = text_model.make_sentence()

        if nonsense is None:
            await client.say("I got Nothing. ¯\_(ツ)_/¯ ")
        else:
            await client.say(""+nonsense)

# Core Functions

# core commands

client.run(TOKEN)

