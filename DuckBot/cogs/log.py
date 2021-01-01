import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def log(self, ctx):

        embed = discord.Embed(title='DuckBot update log', description="Latest updates of the bot:", color=ctx.me.color)

        embed.add_field(name='**`01-01-2021`**', value='Fixed issue that sent 2 un-afk messages when a message was sent', inline=False)

        embed.add_field(name='Suggest an update/feature:', value='Just DM me (the bot) to do that ;)', inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
