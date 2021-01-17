import typing, discord, asyncio, random, datetime
from discord.ext import commands, tasks

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.change_color.start()

    @tasks.loop(minutes=60.0)
    async def change_color(self):
        if datetime.datetime.now().hour == 5:
            color = random.randint(0, 0xFFFFFF)
            await self.bot.get_guild(706624339595886683).get_role(800295689585819659).edit(colour=color)
            channel = self.bot.get_channel(799503231989973022)
            embed = discord.Embed(description=f"Color of the day changed to {color}", color=color)
            await channel.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def cotd(self, ctx, color: typing.Optional[discord.Colour] = discord.Colour.default, tag = "-n"):
        if tag == "-r":
            color = random.randint(0, 0xFFFFFF)
        await self.bot.get_guild(706624339595886683).get_role(800295689585819659).edit(colour=color)
        await ctx.message.delete()
        embed = discord.Embed(description=":sparkles:", color=color)
        await ctx.send(embed=embed, delete_after=3)
        channel = self.bot.get_channel(799503231989973022)
        embed = discord.Embed(description=f"Daily color manually changed to {color}", color=color)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))
