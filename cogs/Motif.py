import discord
from discord.ext import commands
import time

class Motif(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    

  @commands.command()
  async def motif(self, ctx, args):
    
    pass



def setup(bot):
  bot.add_cog(Motif(bot))