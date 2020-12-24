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


    @commands.Cog.listener()
    async def on_message(self, message):
        if 'bee' in message.content.lower():
            await message.add_reaction('🐝')
        if 'xd' in message.content.lower():
            await message.add_reaction('🇽')
            await message.add_reaction('🇩')
        if 'lmao' in message.content.lower():
            await message.add_reaction('🇱')
            await message.add_reaction('🇲')
            await message.add_reaction('🇦')
            await message.add_reaction('🇴')
        if 'lmfao' in message.content.lower():
            await message.add_reaction('🇱')
            await message.add_reaction('🇲')
            await message.add_reaction('🇫')
            await message.add_reaction('🇦')
            await message.add_reaction('🇴')
        if message.guild.me in message.mentions:
            await message.add_reaction('<:AngryPing:791053518375092354>')
        if message.guild.owner in message.mentions:
            await message.add_reaction('<:AngryPing:791053518375092354>')

def setup(bot):
    bot.add_cog(help(bot))
