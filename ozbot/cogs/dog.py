import json, random, discord, aiohttp
from random import randint
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ### DOGGO ###
    # Sends a pic of a dog

    @commands.command(aliases=['dog', 'pup', 'getdog'])
    async def doggo(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
                res = await r.json()  # returns dict
                embed = discord.Embed(title='Here is a dog!', color=random.randint(0, 0xFFFFFF))
                embed.set_image(url=res["message"])
                embed.set_footer(text='by dog.ceo', icon_url='https://i.imgur.com/wJSeh2G.png')
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
