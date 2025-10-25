import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from better_profanity import profanity



load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if profanity.contains_profanity(message.content):
        await message.delete()


bot.run(token,log_handler=handler, log_level=logging.DEBUG)