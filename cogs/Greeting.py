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


def setup(bot):
  bot.add_cog(Greeting(bot))