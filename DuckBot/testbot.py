#DUCKBOT.
#This bot is probably not the best as it is my first one. i'm sorry lol.
#All the stuff here was learnt along the way with no previous experience

#import libraries

import os
import discord
import random
import typing
import json
from random import randint
import discord.channel
import discord.client
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
import requests
from requests.exceptions import RequestException




def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
prefixes[str(guild.id)] = '>'
with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
prefixes.pop(str(guild.id))
with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

@bot.command(aliases=['changeprefix', 'prefixset', 'prefixchange'])
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix

with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)
    await ctx.send(f'Successfully changed the prefix to: **``{prefix}``**')

#GITHUB TOKEN THINGY

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

###### INITIAL CONFIG #####

@bot.event
async def on_ready():
    print ("Bot Onine!")
    print ("Hello I Am " + bot.user.name)
    print ('-----------')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='.help'))

###### COMMANDS #####

### YOUR PING ###
# Tells your ping

@bot.command()
async def ping(ctx):
    await ctx.send("your ping is `" + f'{round (bot.latency * 1000)} ms` ')

### FEL HORSE ###
#sends that picture that Felsha sent me

@bot.command()
async def horse(ctx):
    await ctx.send("https://media.discordapp.net/attachments/760191301894275113/788301744353312798/image0.jpg")

### INSPIREME ###
# Sends an inspirational image

@bot.command()
async def inspireme(ctx):

    # sends GET request to Inspirobot for image url response
    try:
        url = 'http://inspirobot.me/api?generate=true'
        params = {'generate' : 'true'}
        response = requests.get(url, params, timeout=10)
        image = response.text
        embed2 = discord.Embed(title='An inspirational image...', color=random.randint(0, 0xFFFFFF))
        embed2.set_image(url=image)
        embed2.set_footer(text='by inspirobot.me', icon_url='https://inspirobot.me/website/images/inspirobot-dark-green.png')

        await ctx.send(embed=embed2)

    except RequestException:

        await ctx.send('Inspirobot is broken, there is no reason to live.')

##########################
########## TEST ##########
##########################

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 787743717393563698:
            textchannel = bot.get_channel(788226503422902343)
            await textchannel.send('Test message sent to <@349373972103561218>')

########

@bot.command(pass_context=True)
async def name(ctx):
    await ctx.send("{}".format(ctx.message.author.mention))

########

@bot.command()
async def myid(ctx):
	if ctx.message.author.id == ctx.guild.owner_id:
		await ctx.send("{} is your id".format(ctx.message.author.id))
	else:
		await ctx.message.add_reaction('❌')

#########

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

#########
@bot.command()
async def embedcolor(ctx):
	embed = discord.Embed(title='TEST', description='COLOR TEST', color = ctx.me.color)
	await ctx.send(embed=embed)

########################
##### HELP COMMAND #####
########################

bot.remove_command('help')

@bot.command()
async def help(ctx, argument: typing.Optional[str] = "None"):

	if (argument == "None"):

		embed = discord.Embed(title='DuckBot help', description=("Hey {}, Here is a list of arguments:".format(ctx.message.author.mention)), color = 0x6c3e82)

		embed.add_field(name='_ _', value='_ _', inline=False)

		embed.add_field(name='.help commands', value='Show the list of normal commands', inline=False)

		embed.add_field(name='.help testing', value='shows what testing commands do. This list might not be up to date.', inline=False)

		embed.add_field(name='.help', value='Gives this message', inline=False)

		embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')

		embed.add_field(name='_ _', value='_ _', inline=False)

		await ctx.send(embed=embed)

	elif (argument == "commands"):

		embed = discord.Embed(title='DuckBot help', description=("Hey {}, Here is a list of available commands:".format(ctx.message.author.mention)), color = 0x6c3e82)

		embed.add_field(name='_ _', value='_ _', inline=False)

		embed.add_field(name='.horse', value='Requested by Fel - Shows an old photo of Fel.', inline=False)

		embed.add_field(name='.inspireme', value='Returns an AI generated image from Inspirobot.me', inline=False)

		embed.add_field(name='.ping', value="Shwos the bot's ping to the server", inline=False)

		embed.add_field(name='.help', value='Gives a list of arguments', inline=False)

		embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')

		embed.add_field(name='_ _', value='_ _', inline=False)

		await ctx.send(embed=embed)

	elif (argument == "testing"):

		embed = discord.Embed(title='DuckBot help', description=("Hey {}, Here is a list of beta/testing commands. These might not work.".format(ctx.message.author.mention)), color = 0x6c3e82)

		embed.add_field(name='_ _', value='_ _', inline=False)

		embed.add_field(name='.myid', value='Testing permissons for an owner-only command and adding reactions to the original command', inline=False)

		embed.add_field(name='.name', value='Testing on how to send a mention', inline=False)

		embed.add_field(name='.foo', value="Testing on how arguments work", inline=False)

		embed.add_field(name='.embedcolor', value="Testing embed color = top role color", inline=False)

		embed.add_field(name='.help | .help <arg>', value='Testing argument categories and optional arguments', inline=False)

		embed.add_field(name='.help', value='Gives a list of arguments', inline=False)

		embed.add_field(name='_ _', value='_ _', inline=False)

		embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')


	else:

		embed = discord.Embed(title='DuckBot help', description='Incorrect argument. type `.help` for a list of available arguments', color = 0x6c3e82)
		await ctx.send(embed=embed)

####### RUN #######

bot.run(TOKEN)
