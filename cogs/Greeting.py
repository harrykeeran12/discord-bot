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

  @commands.command()
  async def greeting(self, ctx):
    await ctx.send('Greetings!!!')


def setup(bot):
  bot.add_cog(Greeting(bot))