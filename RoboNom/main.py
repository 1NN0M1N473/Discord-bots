### IMPORT LIBRARIES ###
import os
import sys
import json
import random
import requests
import discord
import asyncio
import typing
import traceback
from lib.db import db
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound, MissingRequiredArgument, has_permissions, when_mentioned_or


### DEFINE VARIABLES ###

#prepare database, wait until I have a basic setup before trying to integrate
#postgresql = 'postgresql://robonom:robonom@dcbots/robonom'

#status_string = config.get_string("status") <-- Maybe use config to cycle through status msgs?



### DEFINE TOKEN & PREFIX ###
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

PREFIX= "rn?"
bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=discord.Intents.all())
bot.remove_command("help")



### COGS/EXTENSIONS ###

## AUTOLOAD ##
initial_extensions = ['cogs.help',
                      'cogs.google',
                      'cogs.8ball',
                      'cogs.robonom',
                      'cogs.info',
                      'cogs.say',
                      'cogs.nerdyquote',
                      'cogs.ping',
                      'cogs.modmail']


if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

## MANUAL LOAD ##

@bot.command()
@commands.guild_only()
async def load(ctx, extension):
    if ctx.message.author.id == 645083460658003969:
        bot.load_extension("cogs.{}".format(extension))
        response = await ctx.send("Successfully loaded the specified module.")
        await asyncio.sleep(5)
        await ctx.message.delete()
        await response.delete()
    else:
        response = await ctx.send("You don't have permission to load modules.")
        await asyncio.sleep(5)
        await ctx.message.delete()
        await response.delete()

@bot.command()
@commands.guild_only()
async def unload(ctx, extension):
    if ctx.message.author.id == 645083460658003969:
        bot.unload_extension("cogs.{}".format(extension))
        response = await ctx.send("Successfully unloaded the specified module.")
        await asyncio.sleep(5)
        await ctx.message.delete()
        await response.delete()
    else:
        response = await ctx.send("You don't have permission to unload modules.")
        await asyncio.sleep(5)
        await ctx.message.delete()
        await response.delete()

@bot.command()
@commands.guild_only()
async def reload(ctx, extension):
    if ctx.message.author.id == 645083460658003969:
        bot.unload_extension("cogs.{}".format(extension))
        bot.load_extension("cogs.{}".format(extension))
        response = await ctx.send("Successfully reloaded the specified module.")
        await asyncio.sleep(5)
        await ctx.message.delete()
        await response.delete()
    else:
        response = await ctx.send("You don't have permission to reload modules.")
        await asyncio.sleep(5)
        await ctx.message.delete()
        await response.delete()

### EVENTS ###

## ERROR HANDLING ##
@bot.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
        return

    error = getattr(error, 'original', error)

    if isinstance(error, commands.ExtensionAlreadyLoaded):
        await ctx.send("The specified module has already been loaded.")
        return
    if isinstance(error, commands.ExtensionNotFound):
        await ctx.send("The specified module does not exist.")
        return
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("CommandInvokeError: I might be missing permissions? Make sure I was granted all the requested permissions when added to this server.")
        return
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title='Command Not Found', description='That command or subcommand doesn\'t exist. Do rn?help to see the available commands.', color = 0xFF0000)
        await ctx.send(embed=embed)
        return
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("MissingPermissions Error: I might be missing permissions? Make sure I was granted all the requested permissions when added to this server.")
        return

## ON_READY() ##
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    print(f'-----------------------------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='rn?help'))

### NON_COG COMMANDS ###
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return(quote)

@bot.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

bot.run(TOKEN, reconnect=True)
