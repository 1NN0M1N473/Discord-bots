import discord
import asyncio
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, input):
        if ctx.message.author.id == 645083460658003969:
            await ctx.message.delete()
            await ctx.send(input)
        else:
            response = await ctx.send("Only the creator can impersonate me ;")
            await asyncio.sleep(3)
            await ctx.message.delete()
            await response.delete()
def setup(bot):
    bot.add_cog(Say(bot))
