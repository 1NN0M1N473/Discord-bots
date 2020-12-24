import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("your ping is `" + f'{round (self.bot.latency * 1000)} ms` ')

def setup(bot):
    bot.add_cog(help(bot))
