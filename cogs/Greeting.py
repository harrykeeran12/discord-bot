import discord
import random
import time
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


    # whats up this is my command - Elcurtiso
  @commands.command()
  async def text(self, context, Message):
    await context.send(Message)

  @commands.command()
  async def eightball(self, context, *, question=""):
    if question == "":
      await context.send("Please ask a question!")
    else:
      responses = ['Nope',
                  'Maybe',
                  'Probably',
                  'Good joke',
                  'It could be',
                  'Try Again!',
                  'LMAO, hearing your questions makes me laugh']
      await context.send(f'The eightball says... \n{random.choice(responses)}')
  
  @commands.command(brief = "This button does nothing")
  async def button(self, context):
    random_number = random.randint(0,10)
    if random_number == 1:
      await context.send("Good to have you on recruit, we have to capture this shifty man")
      await context.send(file=discord.File(f'./NDimish nukecodes/Missile Codes (dont look)/Im serious/{random_number}.PNG'))
      time.sleep(2)
      await context.send("This is the file we have on him")
      await context.send(file=discord.File(f'./NDimish nukecodes/Missile Codes (dont look)/Im serious/DONT OPEN.zip'))
      time.sleep(1)
      await context.send("It's your job to decrypt the file and recover the codes")
    else:
      await context.send("This button does nothing! Good job! You wasted your time...")

  @commands.command(brief = "This allows you to destroy your enemies (provided you have the necessary code)")
  async def missile(self, context, password="", target="Secret Hitler"):
    await context.message.delete()
    def encrypt(text):
      return_value = 0
      hm = list(text)
      try:
        for x in range(0, 3):
          return_value = return_value + (len(hm) ** 2 + len(hm) // 4 + ord(hm[x])*ord(hm[x]))
        return return_value
      except:
        return 0
    guess = encrypt(password)
    if guess != 27089:
      await context.send("Sorry, you don't have the necessary credentials!")
    else:
      text1 = await context.send("Target " + target + " acquired")
      time.sleep(2)
      text2 = await context.send(file=discord.File(f'./NDimish nukecodes/Missile Codes (dont look)/Im serious/Fire.jpg'))
      time.sleep(2)
      text3 = await context.send(file=discord.File(f'./NDimish nukecodes/Missile Codes (dont look)/Im serious/Hit.jpg'))
      time.sleep(3)
      text4 = await context.send("Target " + target + " has been eliminated")
      time.sleep(5)
      text5 = await context.send("Clearing away evidence.")
      time.sleep(1)
      text6 = await context.send("Clearing away evidence..")
      time.sleep(1)
      text7 = await context.send("Clearing away evidence...")
      time.sleep(1)
      for x in range(1, 8):
        await f'text{x}'.delete()


  # forget ya boi Elcurtiso... it is I yare yare man
  
  '''
  @bot.command()
  async def translate(ctx):
    
  '''


  # yare yare does work!!!! base
  #currently checking to do while in voice channel
  @commands.command()
  async def yareyare(self, context):
    embed = discord.Embed(title = "Good Grief")
    images = ['https://media.discordapp.net/attachments/791691369017376819/847553650117181500/yare-yare-daze-meme.png?width=881&height=432', 'https://media1.tenor.com/images/da558adfcaaf7eedb607a6c282d123ae/tenor.gif?itemid=12243323', ]
    embed.set_image(url=random.choice(images))
    await context.send(embed = embed)
    voicechk = discord.utils.get(context.bot.voice_clients, guild=context.guild) #ok so discord.utils.get() gets the first item that meets the criteria?
    #print(voicechk)
    source = discord.FFmpegPCMAudio("MP3/Yareyaredaze.mp3")
    # voicechk is the bot id in the channel variable (context is general)
    if (voicechk):
      temp = voicechk.source # this just saves the exact point of the source so it can just be restored really easily
      #print(temp)
      voicechk.pause()
      voicechk.play(source)
      time.sleep(3)
      voicechk.pause()
      voicechk.play(temp)  
    else:
      voice_player = await context.message.author.voice.channel.connect()
      voice_player.play(source)
      time.sleep(3)
      server = context.message.guild.voice_client
      await server.disconnect()
      
  # end yare yare
  
'''
  @greeting.error
  async def greeting_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please add a required argument.')
''' #this works if you dont put in an argument - currently its commented, but this is an example of error handling




def setup(bot):
  bot.add_cog(Greeting(bot))