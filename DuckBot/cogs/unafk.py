import typing, discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.nick.startswith("[AFK]"):
            await message.author.edit(nick=message.author.nick.replace('[AFK] ', ''))
            await message.channel.send(f'{message.author.mention}, **You are no longer afk**', delete_after=5)

def setup(bot):
    bot.add_cog(help(bot))
