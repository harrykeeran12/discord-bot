'''
@bot.command()
async def wiki(ctx, *query):
  if query:  # I'm not sure what the wikipedia api does if you give it an empty string, so this if-statement makes sure something was passed
        query = " ".join(query)  # The rest of the args were passed as a list, so join them back into a string with spaces
        wiki_wiki = wikipediaapi.Wikipedia('en')
        
        
        page_py = wiki_wiki.page(query)

        embed = discord.Embed(title = query, description = (page_py.summary[0: 2000] + '...'), url = page_py.canonicalurl)
        await ctx.send(embed = embed)

'''