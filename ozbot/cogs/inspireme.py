import json, random, discord, aiohttp
from random import randint
from discord.ext import commands
from requests.exceptions import RequestException

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ### INSPIREME ###
    # Sends an inspirational image

    @commands.command(aliases=['inspirobot', 'imageinspire'])
    async def inspireme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://inspirobot.me/api?generate=true') as r:
                res = await r.text()
                embed = discord.Embed(title='An inspirational image...', color=random.randint(0, 0xFFFFFF))
                embed.set_image(url=res)
                embed.set_footer(text='by inspirobot.me', icon_url='https://inspirobot.me/website/images/inspirobot-dark-green.png')
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
