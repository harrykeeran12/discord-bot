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

  @commands.command(description = 'Greets the user')
	# Greets the user try this bruh rippp wth is wrong with line 20? you missed a bracket bruhhhhht ok this should work don't add the str it's gonna display everything  no no ok take ooneut  dir ok this shoudl work don't add str this should work
  async def greeting(self, ctx):
    await ctx.send('Greetings!!! ' + format(ctx.author.display_name))


def setup(bot):
  bot.add_cog(Greeting(bot))