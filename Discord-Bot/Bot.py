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
        'Stephanie Nappo',
        (
            'If security were all that mattered, computer would never be turned on, let alone hooked into '
            'A network with literally millions o fpotential intruders'
        ),
    ]

    security_quotes = [
        'The number one benefit of information technology is that it empowers people to do what they want to do'
    ]

    if message.content == 'whats up':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)

client.run(TOKEN)
