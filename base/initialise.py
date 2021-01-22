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
    if message.content.startswith('.hi'):
        await message.channel.send('hello')

client.run('ODAxOTY5OTMzMTcyMzQyODU0.YAoasw.VxCAD3Q0dfZL0V1s1VQt8y9Padw')
