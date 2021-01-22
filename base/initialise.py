from typing import Iterable, List
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from math import log
import maths_command

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready(): #* response once logged on
    print(f'Connected to Discord as {bot.user}')
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'Connected to Guild: {guild.name} [ID: {guild.id}]')




@bot.command(name='ready', help="Gets a response if the bot's working")
async def on_message(context):  #* ready message
    await context.send('Ready!')

#* startup
load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

print('...',end='\r',flush=True)
bot.run(TOKEN)
