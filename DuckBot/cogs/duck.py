import json, random, discord, requests
from random import randint
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ### DOGGO ###
    # Sends a pic of a dog

    @commands.command(aliases=['getduck', 'quack', 'randomduck'])
    async def duck(self, ctx):
        response = requests.get("https://random-d.uk/api/random?format=json")
        json_data = json.loads(response.text)
        duck = json_data["url"]
        embed = discord.Embed(title='Here is a duck!', color=random.randint(0, 0xFFFFFF))
        embed.set_image(url=duck)
        embed.set_footer(text='by random-d.uk', icon_url='https://avatars2.githubusercontent.com/u/38426912')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
