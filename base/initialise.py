from discord.ext import commands
import os
from dotenv import load_dotenv
from cmds import *



bot = commands.Bot(command_prefix='.')

#* response once logged on
@bot.event
async def on_ready():
    print(f'Connected to Discord as {bot.user}')
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'Connected to Guild: {guild.name} [ID: {guild.id}]')



#* ready message
@bot.command(name='ready', help="Gets a response if the bot's working")
async def on_message(context):
    await context.send('Ready!')


#* startup
load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

print('...',end='\r',flush=True)
bot.run(TOKEN)
