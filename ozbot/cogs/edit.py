import typing, discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['e'])
    async def edit(self, ctx, *, new : typing.Optional[str] = '--d'):
            if ctx.author.guild_permissions.manage_messages == False:
                await ctx.message.add_reaction('🚫')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return
            if ctx.message.reference:
                msg = ctx.message.reference.resolved
                try:
                    if new.endswith("--s"): await msg.edit(content="{}".format(new[:-3]), suppress=True)
                    elif new.endswith('--d'): await msg.edit(content=None, suppress=True)
                    else: await msg.edit(content=new, suppress=False)
                    try: await ctx.message.delete()
                    except discord.Forbidden:
                        return
                except discord.Forbidden:
                    await ctx.message.add_reaction('🚫')
                    await asyncio.sleep(3)
                    try:
                        await ctx.message.delete()
                    except discord.Forbidden:
                        return
                    return
            else:
                await ctx.message.add_reaction('⚠')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return

def setup(bot):
    bot.add_cog(help(bot))
