from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
import logging

client = discord.Client()
description = '''A bot for playing music from Spotify.'''

logging.basicConfig(level=logging.INFO)

command_prefix = "."

bot = commands.Bot(command_prefix=command_prefix, description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Hello!')
load_dotenv()
client.run(os.getenv('TOKEN'))