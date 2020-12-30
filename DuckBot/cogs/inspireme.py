import json, random, discord, requests
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
        try:
            url = 'http://inspirobot.me/api?generate=true'
            params = {'generate' : 'true'}
            response = requests.get(url, params, timeout=10)
            image = response.text
            embed = discord.Embed(title='An inspirational image...', color=random.randint(0, 0xFFFFFF))
            embed.set_image(url=image)
            embed.set_footer(text='by inspirobot.me', icon_url='https://inspirobot.me/website/images/inspirobot-dark-green.png')
            await ctx.send(embed=embed)
        except RequestException:
            await ctx.send('Inspirobot is broken, there is no reason to live.')


def setup(bot):
    bot.add_cog(help(bot))
