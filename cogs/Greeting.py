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
    
  @commands.command(brief = 'Greets the user, addition parameter to summon')
  async def greeting(self, ctx, msg: discord.Member = None):
    '''
    guild = bot.guilds
    members = guild[0].members
    print(members)
    '''
    if msg != None:
      await ctx.send(f'Summon {msg.mention}')
    else:
      await ctx.send(f'Greetings to {ctx.author.display_name} !!!')
  
'''
  @greeting.error
  async def greeting_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please add a required argument.')
''' #this works if you dont put in an argument - currently its commented, but this is an example of error handling


def setup(bot):
  bot.add_cog(Greeting(bot))