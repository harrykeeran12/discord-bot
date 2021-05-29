import discord
from discord.ext import commands

class Greeting(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game('Fruitopia'))
    print("Ready to get Tutti Frutti?")
    print('Excellent Elderberry is online')

  @commands.command(brief = 'Greets the user')
  async def greeting(self, ctx, msg):
    if (msg != self.bot.user):
      await ctx.send(msg)
    else:
      await ctx.send('Greetings to ' + format(ctx.author.display_name) + '!!!')
  
    #if what we mention is not bot then mention that user
   #i dont think you can do that in python? its a js thing prob
   #msg is a string

    
    '''
    try: 
      await ctx.send(member)
    except Exception:
      await ctx.send('Greetings to ' + format(ctx.author.display_name) + '!!!')
    '''
 




def setup(bot):
  bot.add_cog(Greeting(bot))