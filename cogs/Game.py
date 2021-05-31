from discord.ext import commands
import time
import random

diceFaces = [
  ["+-------+",
   "|       |",
   "|   O   |",
   "|       |",
   "+-------+"],
  ["+-------+",
   "|  O    |",
   "|       |",
   "|    O  |",
   "+-------+"],
  ["+-------+",
   "| O     |",
   "|   O   |",
   "|     O |",
   "+-------+"],
  ["+-------+",
   "| O   O |",
   "|       |",
   "| O   O |",
   "+-------+"],
  ["+-------+",
   "| O   O |",
   "|   O   |",
   "| O   O |",
   "+-------+"],
  ["+-------+",
   "| O   O |",
   "| O   O |",
   "| O   O |",
   "+-------+"]
]

class Game(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.players = []
    self.scores = []
  
  @commands.command(brief = 'Join Dice War')
  async def join_dicewar(self, ctx):
    self.players.append(ctx.author.display_name)
    ctx.send(ctx.author.player_name + " joined Dice War.")

  @commands.command(brief = 'Roll dice')
  async def roll_dice(self, ctx):
    for player in self.players:
      roll = []
      val1 = random.randint(1, 6)
      val2 = random.randint(1, 6)
      roll.append(val1)
      roll.append(val2)
      self.scores.append(val1 + val2)
      for row in range(5):
        for val in roll:
          print(diceFaces[val][row], end=" ")
        print()
      time.sleep(1)
    for player in self.players:
      ctx.send(self.players[player] + " Has " + self.scores[player] + " Points!")
    ctx.send(self.players[self.scores.index(max(self.scores))] + " has WON the Game Of Dice War!!!")
  


def setup(bot):
  bot.add_cog(Game(bot))