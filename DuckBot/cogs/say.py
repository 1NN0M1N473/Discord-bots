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

    ##### .s command ####
    # resends the message as the bot

    @commands.command(aliases=['say', 'send', 'foo'])
    @commands.has_permissions(manage_messages=True)
    async def s(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @s.error
    async def s_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep(3)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
