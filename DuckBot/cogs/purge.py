import os
import json
import random
import typing
import discord
import requests
import asyncio
import cleverbotfreeapi
import discord.client
import discord.channel
from random import randint
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from requests.exceptions import RequestException

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['clean', 'purge', 'delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, argument: typing.Optional[int] = "noimput"):
        amount = argument
        if amount != "noimput":
            if amount < 1000:
                await ctx.message.delete()
                await ctx.channel.purge(limit=amount)
            else:
                await ctx.message.delete()
                await ctx.channel.purge(limit=1000)
                await asyncio.sleep(3.5)
                await ctx.send("**[PURGE]** Applied limited of 1000 messages", delete_after=10)
        else:
            await ctx.message.delete()
            await ctx.send("**[PURGE]** The argument must be a number!", delete_after = 5)

    @clear.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep(3)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
