import discord

client = discord.Client()

#* response once logged on
@client.event
async def on_ready():
    print('Logged in!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.hello'):
        await message.channel.send('Ready!')

client.run('')
