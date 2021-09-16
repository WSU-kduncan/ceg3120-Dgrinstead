#!/bin/sh
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

    cyber_security_quotes = [
        'Passwords are like Underwear: dont let people see it, change it very often, and you shouldn't share it with strangers',
        (
            'It takes 20 years to build a reputation, '
            'and few minutes of cyber-incident to ruin it.'
        ),
    ]

    hitchhiker_quotes = [
        ''
        
    ]

    if message.content == 'towel!':
        #response = random.choice(cyber_security_quotes)
        response = random.choice(cyber_security_quotes)
        await message.channel.send(response)

client.run(TOKEN)
