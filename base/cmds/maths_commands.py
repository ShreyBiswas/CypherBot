import discord
from discord.ext import commands
import math

class Maths(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='loglist', help='Logs an entire list of numbers at once!\nFormat: .loglist 1 2 3 4')
    async def on_message(self, ctx, *args: int):
        response = [log(n) for n in args]
        await context.send(str(response))


    #* GENERIC FUNCTION
    @commands.command(name='', help='')
    async def on_message(self, ctx, *args): #replace args, add kwargs if needed
        #do something to args or kwargs

        await context.send(response)

def setup(bot):
    bot.add_cog(Maths(bot))
