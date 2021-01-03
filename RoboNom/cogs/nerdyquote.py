import discord
import random
from discord.ext import commands

class NerdyQuote(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def nerdyquote(self,ctx):
        responses = open('data/nerdyquotes.txt').read().splitlines()
        random.seed(a=None)
        response = random.choice(responses)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(NerdyQuote(bot))
