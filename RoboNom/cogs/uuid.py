import aiohttp
import asyncio
import discord
import json
import random
import typing
from discord.ext import commands
from random import randint

class uuid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uuid():
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.mojang.com/users/profiles/minecraft/1NN0M1N473') as reponse:

                print("Status:", response.status)
                print("Content-Type:", response.headers['content-type'])

                html = await response.text()
                print("Body:", html[:15], "...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(uuid())

def setup(bot):
    bot.add_cog(uuid(bot))
