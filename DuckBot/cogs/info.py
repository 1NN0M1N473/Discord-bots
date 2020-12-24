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
    async def info(self, ctx):
        embed = discord.Embed(title='DuckBot info', description="Here's information about my bot:", color=ctx.me.color)

        # give info about you here
        embed.add_field(name='Author', value='LeoCx1000#9999', inline=False)

        # Shows the number of servers the bot is member of.
        embed.add_field(name='Server count', value="i'm in " + f'{len(self.bot.guilds)}' + " servers", inline=False)

        # give users a link to invite this bot to their server
        embed.add_field(name='Invite',
            value='Invite me to your server [here](https://discord.com/api/oauth2/authorize?client_id=788278464474120202&permissions=8&scope=bot)', inline=False)

        embed.add_field(name='Source code',
            value='My source code can be found [here](https://github.com/1NN0M1N473/Discord-bots/tree/master/DuckBot). Note: it may not be up-to-date', inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
