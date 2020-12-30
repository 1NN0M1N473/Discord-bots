import discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['stop'])
    async def shutdown(self, ctx):
        if ctx.message.author.id == 349373972103561218:
            await ctx.send("🛑 **__Stopping the bot__**")
            await ctx.bot.logout()
        else:
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep(5)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
