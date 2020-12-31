#########################
######## BARRY ##########
########################


### IMPORT LIBRARIES ###

import cogs
import os
import json
import random
import typing
import discord
import discord.channel
import discord.client
import asyncio
import requests
import cleverbotfreeapi
from random import randint
from dotenv import load_dotenv
from discord.ext import commands
from googlesearch import search
from discord.ext.commands import Bot
from requests.exceptions import RequestException



### SET PREFIX, VARIABLES, and TOKEN ###
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), case_insensitive=True, intents=discord.Intents.all())

#Create more secure function so I can push to GitHub without compromising the token

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



### EVENTS ###

#startup recognition
@bot.event
async def on_ready():
    print("Bot is online and ready to go!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='?help | @Barry help'))

### COMMANDS ###

#define main command to load cogs
@bot.command()
@commands.is_owner()
@commands.guild_only()
async def load(ctx, extension):
    if ctx.message.author.id == 645083460658003969:
        bot.load_extension("cogs.{}".format(extension))
        await ctx.message.add_reaction("✅")
        await asyncio.sleep(10)
        await ctx.message.delete()
    else:
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(5)
        await ctx.message.delete()

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction('❌')
        await asyncio.sleep(10)
        await ctx.message.delete()

#define command to unload cogs
@bot.command()
@commands.is_owner()
@commands.guild_only()
async def unload(ctx, extension):
    if ctx.message.author.id == 645083460658003969:
        bot.unload_extension("cogs.{}".format(extension))
        await ctx.message.add_reaction("✅")
        await asyncio.sleep(10)
        await ctx.message.delete()
    else:
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(5)
        await ctx.message.delete()

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("❌")
        await asyncio.sleep(10)
        await ctx.message.delete()

#define command to reload cogs
@bot.command()
@commands.is_owner()
@commands.guild_only()
async def reload(ctx, extension):
    if ctx.message.author.id == 645083460658003969:
        bot.unload_extension("cogs.{}".format(extension))
        bot.load_extension("cogs.{}".format(extension))
        await ctx.message.add_reaction("✅")
        await asyncio.sleep(10)
        await ctx.message.delete()
    else:
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(5)
        await ctx.message.delete()

@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("❌")
        await asyncio.sleep(10)
        await ctx.message.delete()

#configure cogs source dir
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension("cogs.{}".format(filename[:-3]))


### RUN BOT ###

bot.run(TOKEN, reconnect=True)
