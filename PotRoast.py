# https://github.com/NoodleShogun/RostOff/tree/master

# imports
import os
from discord.ext.commands import Bot
import discord
import random

is_prod = os.environ.get('IS_HEROKU', None)



if is_prod:
    BOT_PREFIX = os.environ['prefix']
    TOKEN = os.environ['token']
else:
    BOT_PREFIX = os.environ['prefix']
    TOKEN = os.environ['token']

client = Bot(command_prefix=BOT_PREFIX)
canTTS = True
# Command Functions

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



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
              "Can you die of constipation? I ask because I’m worried about how full of $hit you are."]

    roasts2 = ["To find the amount of Friends you have you must first take the required amount of parameters "
               "you put in divided by the amount needed."]

    if not user:
        await client.say(""+random.choice(roasts2), tts=canTTS)
    else:
        await client.say(""+ user.mention + " " + random.choice(roasts), tts=canTTS)

# Core Functions

# core commands

client.run(TOKEN)
