import typing, discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['pm'])
    @commands.has_permissions(administrator = True)
    async def dm(self, ctx, member : discord.Member, *, message = ""):
        if ctx.message.author.id == 349373972103561218:
            try:
                if ctx.message.attachments:
                    file = ctx.message.attachments[0]
                    myfile = await file.to_file()
                    await member.send(message, file=myfile)
                else:
                    await member.send(message)
                await ctx.message.add_reaction('📬')
                await asyncio.sleep(2.5)
                await ctx.message.clear_reaction('📬')
            except discord.Forbidden:
                await ctx.send(f"{member}'s DMs are closed.")
        else:
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep (5)
            await ctx.message.delete()

    @dm.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep (5)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
