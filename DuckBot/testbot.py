#DUCKBOT.
#This bot is probably not the best as it is my first one. i'm sorry lol.
#All the stuff here was learnt along the way with no previous experience

#import libraries

import os
import json
import random
import typing
import discord
import requests
import discord.client
import discord.channel
from random import randint
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from requests.exceptions import RequestException

bot = commands.Bot(command_prefix='.', case_insensitive=True)

#GITHUB TOKEN THINGY

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#########################################################################
#########################################################################
#########################################################################

@bot.command()
@commands.has_permissions(administrator=True)
async def test(ctx):
    await ctx.send('You are an admin :grin:')

@test.error
async def test_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.message.add_reaction('🚫')



#########################################################################
#########################################################################
#########################################################################

####### RUN #######

bot.run(TOKEN)
