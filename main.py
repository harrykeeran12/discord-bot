import discord
import time
import os
import random
import sqlite3
from discord.ext import commands

#token = os.environ['TOKEN']

token = os.environ['TOKEN2']

bot = commands.Bot(command_prefix='//')
discord_client = discord.Client()
motifs = {}

#doing some sqlite3 database stuff dw about it
conn = sqlite3.connect('motifs.db')
c = conn.cursor()



#----------------------------------------------

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

#Cog handling----------------------------------------------------
@bot.command()
async def load(ctx, extensions):
  bot.load_extension(f'cogs.{extensions}')
  await ctx.send(extensions + ' loaded.')

@bot.command()
async def unload(ctx, extensions):
  bot.unload_extension(f'cogs.{extensions}')
  await ctx.send(extensions + ' unloaded.')

@bot.command()
async def reload(ctx, extensions): #theres a bot.reload_extension y'all know that right? 
  bot.unload_extension(f'cogs.{extensions}')
  bot.load_extension(f'cogs.{extensions}')
  await ctx.send(extensions + ' reloaded.')

#initalise all command file in cogs folder in the start of program
for file in os.listdir("./cogs"):
  if file.endswith('.py'):
    bot.load_extension(f'cogs.{file[:-3]}')
  
#----------------------------------------------------------------



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
              'LMAO, hearing your questions makes me laugh']
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
  source = discord.FFmpegPCMAudio("MP3/Yareyaredaze.mp3")
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


def is_connected(ctx):
    voice_client = ctx.get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()

#this intial code is to see when some one joins and play somthing
# yes i know its spelt announcement. shut up.
#it works with no validation. validation coming
#Edited by NDIMISH

@bot.event
async def on_voice_state_update(Member, Before, After):
  
  #checks if the member is a bot
  if Member.bot:
    return
  
	#external stuff
  mp3array = ["MP3/Join.mp3", "MP3/Join2.mp3", "MP3/Join3.mp3", "MP3/Join4.mp3","MP3/Join5.mp3","MP3/Join6.mp3", "MP3/Join7.mp3"]
  source = discord.FFmpegPCMAudio(random.choice(mp3array))
  conn = sqlite3.connect('motifs.db')
  c = conn.cursor()
  #source = discord.FFmpegPCMAudio('https://cdn.discordapp.com/attachments/791691369017376819/849001866653204480/Join.mp3') huh ok so links apparently do work - this means you could assign ppl different motifs using another command, and get this to auto run it 

# so status includes mute,defen ext. so the line before indicates if the Before
#status is nothing and the after is somthing. the person must have joined
  if Before.channel == None and After.channel != None:
    member_string = str(Member)
    member_string = member_string[0: len(member_string) - 5]
    channel = Member.voice.channel
    c.execute("SELECT name FROM motifs")
    query_names = c.fetchall()
    motif_names = []
    for names in query_names:
      motif_names.append(str(names[0]))

    if member_string in motif_names:
      sql = "SELECT link FROM motifs WHERE name = ?"
      c.execute(sql, [member_string])
      link = c.fetchone()
      source = discord.FFmpegPCMAudio(link[0])
      voice_player = await channel.connect()
      voice_player.play(source)
      time.sleep(3.7)
      await voice_player.disconnect()

    else:
      #connect to voice channel and play. 
      voice_player = await channel.connect()
      voice_player.play(source)
      time.sleep(3.7)
      #leaving channel
      #server = bot.message.guild.voice_client
      await voice_player.disconnect()
    #gonna need context to validate this ngl 


@bot.command(brief = "Allows you to add your own motifs. These will play once you join any call. ")
async def motif(ctx, link):
  try:
    c.execute("""CREATE TABLE motifs(
      name TEXT,
      id INTEGER,
      link TEXT
    )""")
    await ctx.send("New table has been created.")
  except sqlite3.OperationalError:
    full_author = str(ctx.message.author)
    id = full_author[-4: ]
    author = full_author[0: len(full_author) - 5]

    await ctx.send(f'Username = {author}, id is {id}')
    insert = """INSERT INTO motifs(name, id, link)
    VALUES(?, ?, ?)"""
    data = (author, id, link)
    c.execute(insert, data)

    #s_link = str(link)



    c.execute("SELECT name FROM motifs")
    query_names = c.fetchall()
    motif_names = []
    for names in query_names:
      motif_names.append(str(names[0]))


    #print(motif_names)

    if author in motif_names:
      update = "UPDATE motifs SET name = ?, link = ? WHERE name = ?"
      data = (author, link, author)
      c.execute(update, data)
      await ctx.send("Motif has been updated.")
    else: 
      c.execute(insert, data)
      await ctx.send("Motif has been added.")

    conn.commit()
    conn.close()



@bot.command(brief = "Removes a user's motif.")
async def remove_motif(ctx):
  conn = sqlite3.connect('motifs.db')
  c = conn.cursor()
  full_author = str(ctx.message.author)
  author = full_author[0: len(full_author) - 5]
  sql = "DELETE FROM motifs WHERE name = ?"
  c.execute(sql, [author])
  conn.commit()
  await ctx.send(f"User {author} has been deleted from the database.")


@bot.command(brief = "Shows all user's motifs.")
async def show_motifs(ctx):
  conn = sqlite3.connect('motifs.db')
  c = conn.cursor()
  sql = "SELECT * FROM motifs"
  c.execute(sql)
  await ctx.send(c.fetchall())
bot.run(token)

