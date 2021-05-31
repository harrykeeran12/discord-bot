import discord
from discord.ext import commands
import time

class Motif(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()#maybe use event listener instead?
  async def motif(self, ctx):
    voicechk = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    source = discord.FFmpegPCMAudio("MP3/Yareyaredaze.mp3")
    voice = ctx.message.author.voice
    print(voice)
    while(voice == None):
      pass
    if voice != None:
      print(await voice.channel.connect())
      voice_player = await ctx.message.author.voice.channel.connect()
      voice_player.play(source)
      time.sleep(5)
      server = ctx.message.guild.voice_client
      await server.disconnect()



def setup(bot):
  bot.add_cog(Motif(bot))