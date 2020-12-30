#########################
######## BARRY ##########
########################


### IMPORT LIBRARIES ###

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
from cogs.utils import checks, context, db
from cogs.utils.config import Config
import config
import asyncpg



### SET PREFIX, VARIABLES, and TOKEN ###
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), case_insensitive=True, intents=discord.Intents.all())

#Create more secure function so I can push to GitHub without compromising the token

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


### FUNCTIONS ###

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return(quote)



### EVENTS ###

#startup recognition
@bot.event
async def on_ready():
    print("Bot is online and ready to go!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='?help | @Barry help'))

#configure custom prefixes on guild join
@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "?"

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

#remove custom prefix on guild leave
@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

#allow administrators to change bot prefix in their server
@bot.command(aliases=["prefix_change", "set_prefix", "setprefix", "sp"], pass_context=True)
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, *, _prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    if prefixes[str(ctx.guild.id)] != _prefix:

        prefixes[str(ctx.guild.id)] = _prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

            await ctx.send(f"Alright, I've changed the prefix in this server to `{_prefix}`")
    else:
        await ctx.send(f"Sorry, **{ctx.author.display_name}**! That's already my prefix.")

@changeprefix.error
async def changeprefix_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(3)
        await ctx.message.delete()


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








#mouthpiece of Sauron
@bot.command()
async def say(ctx, *, input):
    await ctx.message.delete()
    await ctx.send(input)


#measures latency
@bot.command()
async def ping(ctx):
    await ctx.send("It takes a packet " + f'{round (bot.latency * 1000)}ms ' + " to reach your device from the server.")

#nerdy quote
@bot.command()
async def nerdyquote(ctx):
    responses = open('jokes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

#attack with bees
@bot.command()
async def beeattack(ctx):
    await ctx.send("https://media.giphy.com/media/yIXVnzpoNiE0w/giphy.gif")

#inspirational quote
@bot.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

#chat with barry
@bot.command()
async def barry(ctx, *, input):
    response = cleverbotfreeapi.cleverbot(input)
    await ctx.send(response)

#google search
@bot.command()
async def google(ctx, *, query):
    author = ctx.author.mention
    await ctx.channel.send(f"Here is the number one result for that query {author}!")
    async with ctx.typing():
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            print("User searched for " + query + " and got " + j)
    await ctx.send(j)

#Bot info
@bot.command()
async def info(ctx):
    embed = discord.Embed(title='Information about Barry', description="Here's some information about me", color=ctx.me.color)

    embed.add_field(name='Creator', value='1NN0M1N473#1337', inline=False)

    embed.add_field(name='Server count', value="I'm in " + f'{len(bot.guilds)}' + " servers!", inline=False)

    embed.add_field(name='Invite', value='[Click here](https://discord.com/oauth2/authorize?client_id=788139657711452190&scope=bot) to invite me to your server', inline=False)

    await ctx.send(embed=embed)
### HELP COMMAND ###

bot.remove_command('help')

@bot.command()
async def help(ctx, argument: typing.Optional[str] = "None"):

    if (argument == "None"):

        embed = discord.Embed(title='Barry help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0x00FFFF)

        embed.add_field(name='_ _', value='_ _', inline=False)

        embed.add_field(name='?help commands', value='Shows the commands you can run. Currently the only argument, more to come!', inline=False)

        embed.add_field(name='?help', value='Displays this help screen', inline=False)

        embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')

        embed.add_field(name='_ _', value='_ _', inline=False)

        await ctx.send(embed=embed)


    elif(argument == "commands"):

            embed = discord.Embed(title='Barry help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0x00FFFF)

            embed.add_field(name='_ _', value='_ _', inline=False)

            embed.add_field(name='?ping', value='Measures your latency!', inline=False)

            embed.add_field(name='?help', value='Displays usable commands', inline=False)

            embed.add_field(name='?quote', value='Fetches a random quote from the ZenQuote API', inline=False)

            embed.add_field(name='?nerdyquote', value="Fetches a random programming-themed quote", inline=False)

            embed.add_field(name='?beeattack', value="Summons a horde of angry bees, use with caution", inline=False)

            embed.add_field(name='?barry <say something>', value="Engage in conversation with the bot; responses not guaranteed to make sense", inline=False)

            embed.add_field(name='_ _', value='_ _', inline=False)

            embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')

            await ctx.send(embed=embed)

    else:

        embed = discord.Embed(title='Barry help', description='No command found. What exactly are you trying to accomplish? Run ?help again.', color = 0xFF0000)

        embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')

        await ctx.send(embed=embed)


### RUN BOT ###

bot.run(TOKEN)
