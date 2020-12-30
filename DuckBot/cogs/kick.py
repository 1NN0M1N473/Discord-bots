import typing, discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason: typing.Optional[str] = "No reason specified"):
        if member.top_role < ctx.author.top_role:
            if member.guild_permissions.kick_members == False:
                await member.send(f"""**{ctx.message.author}** has kicked **you** from **{ctx.guild.name}**
**Reason:** `{reason}`""")
                await member.kick(reason=reason)
                await ctx.send(f"""**{ctx.message.author}** has kicked **{member}**!
**Reason:** `{reason}`""")
            else:
                await ctx.send(f"**{ctx.message.author}**, you can't kick another moderator!", delete_after=10)
                await ctx.message.delete()

        else:
            await ctx.send(f"**{member}** is higher than you in role hierarchy!", delete_after=10)
            await asyncio.sleep (2)
            await ctx.message.delete()

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep (2)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
