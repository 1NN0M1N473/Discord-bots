import json, random, discord, requests
from random import randint
from discord.ext import commands


class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ### CAT ###
    # Sends a pic of a cat

    @commands.command(aliases=['meow', 'kitty', 'getcat'])
    async def cat(self, ctx):
        response = requests.get("https://aws.random.cat/meow")
        json_data = json.loads(response.text)
        cat = json_data["file"]
        embed = discord.Embed(title='Here is a cat!', color=random.randint(0, 0xFFFFFF))
        embed.set_image(url=cat)
        embed.set_footer(text='by random.cat', icon_url='https://purr.objects-us-east-1.dream.io/static/img/random.cat-logo.png')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
