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





@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Dark Souls III"))


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
async def roast(Discuser: discord.User=None):
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
              "Can you die of constipation? I ask because I’m worried about how full of $hit you are.",
              "If laughter is the best medicine, your face must be curing the world.",
              "I’ve seen people like you before, but I had to pay admission.",
              "I’m sorry, was I meant to be offended? The only thing offending me is your face.",
              "Stupidity’s not a crime, so you’re free to go.",
              "If I had a face like yours I’d sue my parents.",
              "You’re not stupid; you just have bad luck when thinking.",
              "The zoo called. They’re wondering how you got out of your cage?",
              "Jesus loves you… but everyone else thinks you’re an asshole.",
              "I was hoping for a battle of wits but you appear to be unarmed.",
              "Aww, it’s so cute when you try to talk about things you don’t understand.",
              "I don’t know what makes you so stupid, but it really works.",
              "You are proof that evolution can go in reverse.",
              "Brains aren’t everything. In your case they’re nothing.",
              "I thought of you today. It reminded me to take the garbage out.",
              "When you were born, the doctor came out to the waiting room and said to your dad, \"I’m very sorry. We did everything we could. But he pulled through.\"",
              "I’d slap you but I don’t want to make your face look any better.",
              "Gay? I’m straighter than the pole your mom dances on.",
              "I just stepped in something that was smarter than you… and smelled better too.",
              "You bring everyone a lot of joy, when you leave the room.",
              "I could eat a bowl of alphabet soup and shit out a smarter statement than that.",
              "I don’t exactly hate you, but if you were on fire and I had water, I’d drink it.",
              "Shock me, say something intelligent.",
              "I had a nightmare. I dreamed I was you.",
              "I am not anti-social. I just don’t like you.",
              "Your ambition outweighs your relevant skills.",
              "You are proof that God has a sense of humor."
              ]

    roasts2 = ["To find the amount of Friends you have you must first take the required amount of parameters "
               "you put in divided by the amount needed."]

    if Discuser == client.user:
        client.say(""+ discord.Message.author + "Nice try but I can't roast myself.", tts=canTTS)

    elif not Discuser:

        await client.say(""+random.choice(roasts2), tts=canTTS)
    else:
        await client.say(""+ Discuser.mention + " " + random.choice(roasts), tts=canTTS)

# Core Functions




# core commands

client.run(TOKEN)
