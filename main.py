import discord
import time
import os
import random
from discord.ext import commands


global last_message #do we really need this global variable?

last_message = ""
token = os.environ['TOKEN']

bot = commands.Bot(command_prefix='//')
discord_client = discord.Client()
motifs = {}

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

#testing cogs--------------------------------------------------------
@bot.command()
async def load(ctx, extensions):
  bot.load_extension(f'cogs.{extensions}')
  await ctx.send(extensions + ' loaded.')

@bot.command()
async def unload(ctx, extensions):
  bot.unload_extension(f'cogs.{extensions}')
  await ctx.send(extensions + ' unloaded.')

@bot.command()
async def reload(ctx, extensions):
  bot.unload_extension(f'cogs.{extensions}')
  bot.load_extension(f'cogs.{extensions}')
  await ctx.send(extensions + ' reloaded.')

#initalise all command file in cogs folder in the start of program
for file in os.listdir("./cogs"):
  if file.endswith('.py'):
    bot.load_extension(f'cogs.{file[:-3]}')
    

#--------------------------------------------------------------------

# whats up this is my command - Elcurtiso
@bot.command()
async def text(context, Message):
    await context.send(Message)

@bot.command()
async def eightball(context, *, question):
  responses = ['Nope',
              'Maybe',
              'Probably',
              'Good joke',
              'It could be',
              'Try Again!',
              'LMAO, hearing your questions makes me laugh.ewww',
              ' Secret 9th response == Nathan is not as cool as Curtis.']
  await context.send(f'The eightball says... \n{random.choice(responses)}')

# forget ya boi Elcurtiso... it is I yare yare man
'''
@bot.command()
async def translate(ctx):
  
'''







# yare yare does work!!!! base
#currently checking to do while in voice channel
# line 204 for idle disconnect timing
@bot.command()
async def yareyare(context):
  embed = discord.Embed(title = "Good Grief")
  images = ['https://media.discordapp.net/attachments/791691369017376819/847553650117181500/yare-yare-daze-meme.png?width=881&height=432', 'https://media1.tenor.com/images/da558adfcaaf7eedb607a6c282d123ae/tenor.gif?itemid=12243323', ]
  embed.set_image(url=random.choice(images))
  await context.send(embed = embed)
  voicechk = discord.utils.get(context.bot.voice_clients, guild=context.guild) #ok so discord.utils.get() gets the first item that meets the criteria?
  #print(voicechk)
  source = discord.FFmpegPCMAudio("Yareyaredaze.mp3")
  # voicechk is the bot id in the channel variable (context is general)
  if (voicechk):
		# this is some great stuff
    #the original if statement already checks if its in the channel + we are pausing it anyway
		# now playing doesnt mean anything tho
    #the if statement voicechk works fine we tested that its everything below
		#what does the else stuff do?
    #thats for when the bot isnt currently in the channel, it adds the bot and plays the clip
		# could you loop the queue, then add the yare yare thing, then skip to it, then unloop? technically that would work?
    #the issue is that when a song plays we pause it and yareyare plays but the song doesnt resume
		#creating a new event loop or something maybe? 

		#try print now_playing? just to see if it actually does anything? 
    #ok

		#we have learnt that now playing doesnt do anything
    #then how do we get the info of the current song?

		#it doesnt mean anything though, there might be another way to return it 
		# we can use source
		# just invoking source prints the source i think? 
    #you may be right without a variable
		#thats just gonna play yareyare, but we wanna do voicechk(source) i think? cos its an attribute? 

    #ok fixed this too

    temp = voicechk.source # this just saves the exact point of the source so it can just be restored really easily
    #print(temp)
    voicechk.pause()
    voicechk.play(source)
    time.sleep(5)
    voicechk.pause()
    voicechk.play(temp)

    
  else:
    voice_player = await context.message.author.voice.channel.connect()
    voice_player.play(source)
    time.sleep(5)
    server = context.message.guild.voice_client
    await server.disconnect()
		
# end yare yare
'''
@bot.command()
async def motif(ctx, audiourl): # what this needs to do - check if the person writing has a motif, then plays the motif when they enter a call
  if ctx.message.author in motifs:
    voicechk = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    source = discord.FFmpegPCMAudio(motifs.get(str(ctx.message.author)))
    if (voicechk != None):
      temp = voicechk.now_playing
      voicechk.now_playing.pause()
      voicechk.play(source)
      voicechk.now_playing = temp
      voicechk.resume()
  else:
    motifs.update({str(ctx.message.author), str(audiourl)})
    ctx.send('Run the command again.') # this makes sure that the motif is stored into the dictionary
'''



bot.run(token)

