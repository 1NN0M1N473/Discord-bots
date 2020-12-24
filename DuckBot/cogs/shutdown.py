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

    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.id == 349373972103561218:
            await ctx.send("🛑 **__Stopping the bot__**")
            await ctx.bot.logout()
        else:
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep(5)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
