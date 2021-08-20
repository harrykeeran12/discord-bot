import time


# this is a test to see if the . thing works

@bot.command()
async def yareyare(context, Member, Before, After):

	if Member.bot:
		return
	
	voicechk = discord.utils.get(context.bot.voice_client, guild =context.guild)
	source = discord.FFmpegPCMAudio("MP3/Join.mp3")

	if Before.channel == None and After.channel != None:
		if voicechk:
			temp = voicechk.source # this just saves the exact point of the source so it can just be restored really easily
			#print(temp)
			voicechk.pause()
			voicechk.play(source)
			time.sleep(3.7)
			voicechk.pause()
			voicechk.play(temp)
			
		else:
			voice_player = await context.message.author.voice.channel.connect()
			voice_player.play(source)
			time.sleep(5)
			server = context.message.guild.voice_client
			await server.disconnect()


@bot.event
async def on_voice_state_update(Member, Before, After):
  
  #checks if the member is a bot
  if Member.bot:
    return
  
	#external stuff
  voicechk = is_connected()
  source = discord.FFmpegPCMAudio("MP3/Join.mp3")

# so status includes mute,defen ext. so the line before indicates if the Before
#status is nothing and the after is somthing. the person must have joined
  if Before.channel == None and After.channel != None:
 # code below not working
      # the code below will check if the bot is in a voice channel
    #voicechk = discord.utils.get(context.bot.voice_client, guild =context.guild)
		# for refrence...
		# voicechk = discord.utils.get(context.bot.voice_clients, guild=context.guild)

    #the code below will check if the bot channel is same as joining member channel
    if voicechk:
      if voicechk.voice.channel == Member.voice.channel:
          temp = voicechk.source 
          voicechk.pause()
          voicechk.play(source)
          time.sleep(5)
          voicechk.pause()
          voicechk.play(temp)
          return
          # the code below means if bot not in new comer voice channel. leave the channel and join new comer voice channel
      else:
        voicechk.channel.disconnect()
    channel = Member.voice.channel
    #connect to voice channel and play. 
    voice_player = await channel.connect()
    voice_player.play(source)
    time.sleep(3.7)
    #leaving channel
    #server = bot.message.guild.voice_client
    await voice_player.disconnect()
