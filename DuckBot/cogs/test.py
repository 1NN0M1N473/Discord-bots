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
import aiohttp

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        if ctx.message.author.id == 349373972103561218:
            await ctx.send(self.bot.activity)

    @test.error
    async def test_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"""```⚠ {error}```""")
            await asyncio.sleep(3)
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                return
            return

def setup(bot):
    bot.add_cog(help(bot))
