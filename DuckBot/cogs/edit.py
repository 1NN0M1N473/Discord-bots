import typing, discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def edit(self, ctx, id : typing.Optional[int] = "none", *, new : typing.Optional[str] = '--d'):
            if ctx.message.author.id != 349373972103561218:
                await ctx.message.add_reaction('🚫')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return
            if id == "none":
                await ctx.message.add_reaction('🔢')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return
            if len(f'{id}') != 18:
                await ctx.message.add_reaction('#️⃣')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return
            try:
                msg = await ctx.channel.fetch_message(id)
                try:
                    if new.endswith("--s"):
                        await msg.edit(content="{}".format(new[:-3]), suppress=True)
                    else:
                        if msg == '--d': await msg.edit(content=None, suppress=False)
                        else: await msg.edit(content=new, suppress=False)
                    try:
                        await ctx.message.delete()
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
            except discord.NotFound:
                await ctx.message.add_reaction('⁉')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return
            except discord.Forbidden:
                await ctx.message.add_reaction('⛔')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return






def setup(bot):
    bot.add_cog(help(bot))
