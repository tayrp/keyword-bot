import discord
import keyword
from discord import Client
from discord.ext import commands
intents = discord.Intents.default()
intents.typing = True
intents.presences = True

client = commands.Bot(command_prefix = 'tia.', intents=intents)

keywords = ["keyword yes", "keyword no"]

@client.event
async def on_ready():
    print("Tia is now online")
    print("Searching for Keywords")
    print("----------------------")

@bot.event
async def on_message(message):
      message_text = message.content.strip().upper()
      if keyword in message_text:
            await bot.send_message(message.channel, "'{}' was said".format(keyword))