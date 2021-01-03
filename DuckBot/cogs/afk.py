import typing, discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def afk(self, ctx):
        nick = f'{ctx.author.nick}'
        if nick == 'None':
            nick = f'{ctx.author.name}'
        else:
            nick = nick
        if nick.startswith("[AFK] "):
            await ctx.message.delete()
            try:
                await ctx.author.edit(nick=nick.replace('[AFK] ', ''))
                await ctx.send(f'{ctx.author.mention}, **You are no longer afk**', delete_after=15)
            except discord.Forbidden:
                await ctx.send(f'🚫 Bot does not have enough permissions, or bot not high enough in role hierarchy 🚫', delete_after=20)
        else:
            await ctx.message.delete()
            try:
                await ctx.author.edit(nick=f'[AFK] {nick}')
                await ctx.send(f'{ctx.author.mention}, **You are afk**', delete_after=15)
            except discord.Forbidden:
                await ctx.send(f'🚫 Bot does not have enough permissions, or bot not high enough in role hierarchy 🚫', delete_after=20)

def setup(bot):
    bot.add_cog(help(bot))
