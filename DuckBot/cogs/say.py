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
        if ctx.channel.permissions_for(ctx.author).mention_everyone:
            await ctx.send(msg)
        else:
            await ctx.send(msg, allowed_mentions = discord.AllowedMentions(everyone = False))

def setup(bot):
    bot.add_cog(help(bot))
