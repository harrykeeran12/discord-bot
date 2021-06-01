from discord.ext import commands
import discord
import time
import random

class Game(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.players = []
    self.scores = []
  
  @commands.command(brief = 'Join Dice War')
  async def join_dicewar(self, ctx):
    self.players.append(ctx.author.display_name)
    await ctx.send(ctx.author.display_name + " joined the Dice War.")

  @commands.command(brief = 'Quit Dice War')
  async def quit_dicewar(self, ctx):
    try:
      self.players.remove(ctx.author.display_name)
      await ctx.send(ctx.author.display_name + " Quit the Dice War.")
    except:
      await ctx.send(ctx.author.display_name + " is not in the game.")

  @commands.command(brief = 'Empty all players from Dice War')
  async def reset_dicewar(self, ctx):
    self.players = []
    await ctx.send("All players has been emptied from Dice War.")

  @commands.command(brief = 'Roll dice')
  async def roll_dice(self, ctx):
    if len(self.players) != 0:
      for player in self.players:
        listScore = ""
        roll = []
        self.scores = []
        val1 = random.randint(1, 6)
        val2 = random.randint(1, 6)
        roll.append(val1)
        roll.append(val2)
        self.scores.append(val1 + val2)
        await ctx.send(player + " Is Rolling...")
        time.sleep(1)

        for val in roll:
          await ctx.send(file=discord.File(f'./diceface/face{val}.png'))
      
      for i in range(len(self.players)):
        listScore = listScore + self.players[i] + " Has " + str(self.scores[i]) + " Points!" + "\n"
      await ctx.send("----------ScoreBoard----------")
      await ctx.send(listScore)
      await ctx.send(self.players[self.scores.index(max(self.scores))] + " has WON the Game Of Dice War!!!")
    else:
      await ctx.send("No players")
    

def setup(bot):
  bot.add_cog(Game(bot))