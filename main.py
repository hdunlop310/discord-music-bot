import os
import discord
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discordSuperUtils import MusicManager
import ffmpeg 


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")
SPOTIFY_PUBLIC = os.getenv("SPOTIFY_PUBLIC")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")

bot = commands.Bot(command_prefix = "!")
MusicManager = MusicManager(bot, client_id=SPOTIFY_PUBLIC,
                                  client_secret=SPOTIFY_SECRET, spotify_support=True)

@bot.command(name = "hello")
async def greet(ctx):
    await ctx.send("Hello, " + ctx.message.author.name + "!")

@bot.command(name = "p")
async def play(ctx, query):
    print(query)
    if await MusicManager.join(ctx):
        await ctx.send("Joined Voice Channel: {}".format(ctx.message.author.voice.channel))
        await play_music(ctx, query)




@MusicManager.event()
async def on_play(ctx, player):
    await ctx.send(f"Playing {player}")


@bot.command()
async def play_music(ctx, query: str):
    print("this is where spotify link is used to play music")


bot.run(DISCORD_TOKEN)