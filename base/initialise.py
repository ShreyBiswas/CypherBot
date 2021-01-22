import discord
import os
from dotenv import load_dotenv

client = discord.Client()

#* response once logged on
@client.event
async def on_ready():
    print(f'Connected to Discord as {client.user}')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'Connected to Guild: {guild.name} with ID {guild.id}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.hello'):
        await message.channel.send('Ready!')



load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

print('...',end='\r',flush=True)
client.run(TOKEN)
