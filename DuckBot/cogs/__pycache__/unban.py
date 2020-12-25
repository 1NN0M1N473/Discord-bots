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
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason: typing.Optional[str] = "No reason specified"):
        await member.kick(reason=reason)
        await ctx.send(f'Member **{member}** unban. Reason: `{reason}`')

def setup(bot):
    bot.add_cog(help(bot))
