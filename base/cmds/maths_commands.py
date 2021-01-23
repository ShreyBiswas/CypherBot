import math




@bot.command(name='loglist', help='Logs an entire list of numbers at once!\nFormat: .loglist 1 2 3 4')
async def on_message(context, *args: int):
    response = [log(n) for n in args]
    await context.send(str(response))


#* GENERIC FUNCTION
@bot.command(name='', help='')
async def on_message(context, *args): #replace args, add kwargs if needed
    #do something to args or kwargs

    await context.send(response)

