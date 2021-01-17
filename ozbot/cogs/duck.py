import json, random, discord, aiohttp
from random import randint
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ### DOGGO ###
    # Sends a pic of a dog

    @commands.command(aliases=['getduck', 'quack', 'randomduck'])
    async def duck(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://random-d.uk/api/random?format=json') as r:
                res = await r.json()  # returns dict
                embed = discord.Embed(title='Here is a duck!', color=random.randint(0, 0xFFFFFF))
                embed.set_image(url=res["url"])
                embed.set_footer(text='by random-d.uk', icon_url='https://avatars2.githubusercontent.com/u/38426912')
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
