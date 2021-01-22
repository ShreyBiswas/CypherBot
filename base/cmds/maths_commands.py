import math




@bot.command(name='loglist', help='Logs an entire list of numbers at once!\nFormat: .loglist 1 2 3 4')
async def on_message(context, *args: int):
    answer = [log(n) for n in args]
    await context.send(str(answer))



@bot.command(name='', help='')
async def on_message(context, *args):
    #
    await context.send(str(reply))

