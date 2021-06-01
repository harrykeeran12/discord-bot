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
@bot.command(brief = "Loads cog into the bot")
async def load(ctx, extensions):
  bot.load_extension(f'cogs.{extensions}')
  await ctx.send(extensions + ' loaded.')

@bot.command(brief = "Unloads cog from the bot")
async def unload(ctx, extensions):
  bot.unload_extension(f'cogs.{extensions}')
  await ctx.send(extensions + ' unloaded.')

@bot.command(brief = "Reloads cog into the bot")
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









# code below is all for motif bot
#it works with no validation. validation coming
#Edited by NDIMISH and harry9

@bot.event
async def on_voice_state_update(Member, Before, After):
  
  #checks if the member is a bot
  if Member.bot:
    return
  
	#external stuff
  mp3array = ["MP3/Join.mp3", "MP3/Join2.mp3", "MP3/Join3.mp3", "MP3/Join4.mp3","MP3/Join5.mp3","MP3/Join6.mp3", "MP3/Join7.mp3"]
  source = discord.FFmpegPCMAudio(random.choice(mp3array))

  #get member id. used to search through database

  member_string = str(Member)
  member_string = int(member_string[-4: ])
  conn = sqlite3.connect('motifs.db')
  c = conn.cursor()
  statement = 'SELECT active FROM motifs WHERE id = ?'
  c.execute(statement, [member_string])
  state_of_active_motif = c.fetchone()
  if state_of_active_motif == 0:
    return
 

# so status includes mute,defen ext. so the line before indicates if the Before
#status is nothing and the after is somthing. the person must have joined
  if Before.channel == None and After.channel != None:
    channel = Member.voice.channel
    c.execute("SELECT id FROM motifs")
    query_id = c.fetchall()
    motif_names = []
    for names in query_id:
      motif_names.append(int(names[0]))

# member string is the id of the messege user
    if member_string in motif_names:
      sql = "SELECT link FROM motifs WHERE id = ?"
      c.execute(sql, [member_string])
      link = c.fetchone()
      if link != "None":
        source = discord.FFmpegPCMAudio(link[0])
    
    #connect to voice channel and play. 
    voice_player = await channel.connect()
    voice_player.play(source)
    time.sleep(4)
    #leaving channel
    #server = bot.message.guild.voice_client
    await voice_player.disconnect()
  #gonna need context to validate this ngl 









@bot.command(brief = "Allows you to add your own motifs. These will play once you join any call. ")
async def motif(ctx, link):
  conn = sqlite3.connect('motifs.db')
  c = conn.cursor()
  
  if 'mp3' not in link:
    await ctx.send(f'Sorry {ctx.author} you need to send me a .mp3 file')
    return

  # to get member id 
  full_author = str(ctx.message.author)
  id_name = int(full_author[-4:])
  author = full_author[0: len(full_author) - 5]
  active = 1

  #incase of failure make a new table
  try:
    c.execute("""CREATE TABLE motifs(
      name TEXT,
      id INTEGER,
      link TEXT,
      active INTEGER
    )""")
    await ctx.send("New table has been created.")
  except sqlite3.OperationalError:

# to chck if member in database
    c.execute("SELECT id FROM motifs")
    query_ids = c.fetchall()
    motif_ids = []
    for id in query_ids:
      motif_ids.append(int(id[0]))
      
    

# if in database update link else add
    if id_name in motif_ids:
      update = "UPDATE motifs SET link = ? WHERE id = ?"
      data = (link, id_name)
      c.execute(update, data)
      await ctx.send("Motif has been updated.")
    else: 
      insert = """INSERT INTO motifs(name, id, link, active)
      VALUES(?, ?, ?, ?)"""
      data = (author, id_name, link, active)
      c.execute(insert, data)
      await ctx.send("Motif has been added.")

    conn.commit()
    conn.close()










@bot.command(brief = "Removes a user's motif.")
async def remove_motif(ctx):
  #connects to db, then finds the author
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









@bot.command(brief = "Sets your motif on active")
async def on_motifs(ctx):
  #get the id of user
  id_here = str(ctx.message.author)
  id_here = int(id_here[-4:])
  #make database connection
  conn = sqlite3.connect('motifs.db')
  c = conn.cursor()
  # check if user has a datbase name
  c.execute('SELECT id FROM motifs')
  id_many = c.fetchall()
  if id_here not in id_many:
    await ctx.send(f'motif not in database for {ctx.message.author}')
    return

    # change active state
  sql = "UPDATE motifs SET active = 1 WHERE id = ?"
  c.execute(sql, [id_here])
  await ctx.send(f'motif deactivated for {ctx.message.author}')
  conn.commit()









@bot.command(brief = "Sets your motif on deactive")
async def off_motifs(ctx):
  #get the id of user
  id_here = str(ctx.message.author)
  id_here = int(id_here[-4:])
  #make database connection
  conn = sqlite3.connect('motifs.db')
  c = conn.cursor()
  # check if user has a datbase name
  c.execute('SELECT id FROM motifs')
  id_many = c.fetchall()
  if id_here not in id_many:
    await ctx.send(f'motif not in database for {ctx.message.author}')
    return
    # change active state to off
  sql = "UPDATE motifs SET active = 0 WHERE id = ?"
  c.execute(sql, [id_here])
  await ctx.send(f'motif deactivated for {ctx.message.author}')
  conn.commit()



#all code must be above this
bot.run(token)