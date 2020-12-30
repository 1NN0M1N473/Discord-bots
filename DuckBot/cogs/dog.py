import json, random, discord, requests
from random import randint
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ### DOGGO ###
    # Sends a pic of a dog

    @commands.command(aliases=['dog', 'pup', 'getdog'])
    async def doggo(self, ctx):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        json_data = json.loads(response.text)
        doggo = json_data["message"]
        embed = discord.Embed(title='Here is a dog!', color=random.randint(0, 0xFFFFFF))
        embed.set_image(url=doggo)
        embed.set_footer(text='by dog.ceo', icon_url='https://i.imgur.com/wJSeh2G.png')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
