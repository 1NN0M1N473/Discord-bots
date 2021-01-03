import discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ##### .s command ####
    # resends the message as the bot

    @commands.command(aliases=['say', 'send', 'foo'])
    async def s(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @s.error
    async def s_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction('🚫')

def setup(bot):
    bot.add_cog(help(bot))
