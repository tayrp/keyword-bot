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

@client.event
async def on_message(message):
    for t in range(len(keywords)):
      message_text = message.content
      if keywords in message.content:
        if (message.content == 'coolmsg'):
            await client.send_message(message.channel, "'{}' was said".format(keyword))