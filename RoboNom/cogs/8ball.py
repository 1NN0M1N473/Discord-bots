import random
import discord
from discord.ext import commands

class _8ball(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, input):
        responses = open('data/8ball.txt').read().splitlines()
        random.seed(a=None)
        response = random.choice(responses)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(_8ball(bot))
