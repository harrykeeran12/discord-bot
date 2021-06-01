import main.py
# this is code current working on. indent into 159
 # code below not working
  
    # the code below will check if the bot is in a voice channel

    voicechk = discord.utils.get(context.bot.voice_client, guild =context.guild)
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





            #First we check if the person is in the database
    c.execute('SELECT id FROM motifs')
    members_id = c.fetchall()
    if id not in members_id:

      author = full_author[0: len(full_author) - 5]
      active = 1
      await ctx.send(f'Username = {author}, id is {id}')