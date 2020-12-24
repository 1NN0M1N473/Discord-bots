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
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            if after.channel.id == 787743717393563698:
                textchannel = self.bot.get_channel(788226503422902343)
                await textchannel.send('Hey <@349373972103561218>, Someone joined a voice channel!')

def setup(bot):
    bot.add_cog(help(bot))
