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

    @commands.command(aliases=['inspirequote', 'quote', 'inspire', 'motivateme'])
    async def motivate(self, ctx):
        response = requests.get("https://www.affirmations.dev/")
        json_data = json.loads(response.text)
        affirm = json_data["affirmation"]
        await ctx.send(affirm)

def setup(bot):
    bot.add_cog(help(bot))
