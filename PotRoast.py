# https://github.com/NoodleShogun/RostOff/tree/master

# imports

import discord
import random

# variables and other stuff
TOKEN = 'NDM4MDgyMTAyOTUzNzcxMDEw.Db_buQ._9gFilYm4oRyurUMPACaJ4DrLxs'
client = discord.Client()

roast1 = ["If I wanted to Commit Suicide I'd climb your Ego and Jump to your IQ", "Ur Mom Gay", 
          "One might say that you lack an ability to process reasonable explanations for sticky situations"
         ]



# Command Functions
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

# Core Functions
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
