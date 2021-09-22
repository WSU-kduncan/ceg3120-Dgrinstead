import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    cybersecurity_quotes = [
        'Technology trust is a good thing, but control is a better one',
        'Stephane Nappo',
        (
            'If security were all that mattered, computers would never be turned on, let alone hooked into' 
           ' a network with literally millions of potential intruders'
        ),
    ]

    security_quotes = [
        'Security used to be an inconvenience sometimes, but now its a necessity all the time'
    ]

    if message.content == 'whats up':
        #response = random.choice(cybersecurity_quotes)
        response = random.choice(security_quotes)
        await message.channel.send(response)

client.run(TOKEN)
