import json, discord, requests
from random import randint
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['inspirequote', 'quote', 'inspire', 'motivateme'])
    async def motivate(self, ctx):
        response = requests.get("https://www.affirmations.dev/")
        json_data = json.loads(response.text)
        affirm = json_data["affirmation"]
        await ctx.send(affirm)

def setup(bot):
    bot.add_cog(help(bot))
