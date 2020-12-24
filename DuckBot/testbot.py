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
import cleverbotfreeapi
import discord.client
import discord.channel
from random import randint
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from requests.exceptions import RequestException

intents = discord.Intents.default() # Enable all intents except for members and presences
intents.members = True  # Subscribe to the privileged members intent.



####################################

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)


@bot.command(aliases=["prefix_change", "set_prefix", "setprefix", "sp"], pass_context=True)
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, *, _prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    if prefixes[str(ctx.guild.id)] != _prefix:

        prefixes[str(ctx.guild.id)] = _prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

            await ctx.send(f"Prefix set to `{_prefix}`!")
    else:
        await ctx.send(f"That is already the prefix, **{ctx.author.display_name}**.")


@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "."

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


#GITHUB TOKEN THINGY

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

###### INITIAL CONFIG #####

@bot.event
async def on_ready():
    print ("Bot Online!")
    print ("Hello I Am " + bot.user.name)
    print ('-----------')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='.help'))

##### .s command ####
# Same as FOO but with less lag because
# it comes before than the on_message
# event. (only I can use it tho)

@bot.command(aliases=['say', 'send'])
async def s(ctx, *, msg):
    if ctx.message.author.id == ctx.guild.owner_id:
        await ctx.message.delete()
        await ctx.send(msg)
    else:
        await ctx.message.add_reaction('🚫')


##### FUNCTIONS #####

def get_aff():
    response = requests.get("https://www.affirmations.dev/")
    json_data = json.loads(response.text)
    affirm = json_data["affirmation"]
    return(affirm)

##### GET DOG

def dog_img():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    json_data = json.loads(response.text)
    doggo = json_data["message"]
    return(doggo)

##### GET CAT

def cat_img():
    response = requests.get("https://aws.random.cat/meow")
    json_data = json.loads(response.text)
    cat = json_data["file"]
    return(cat)

####### EVENTS #######

##### JOINPING

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 787743717393563698:
            textchannel = bot.get_channel(788226503422902343)
            await textchannel.send('Hey <@349373972103561218>, Someone joined a voice channel!')

##### BEE reaction 🇽 🇩

@bot.event
async def on_message(message):
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
    await bot.process_commands(message)


############################
######### COMMANDS #########
############################

### motivate ###
# random motivational quotes

@bot.command(aliases=['inspirequote', 'quote', 'inspire', 'motivateme'])
async def motivate(ctx):
    affirm = get_aff()
    await ctx.send(affirm)

### DOGGO ###
# Sends a pic of a dog

@bot.command(aliases=['dog', 'pup', 'getdog'])
async def doggo(ctx):
    image = dog_img()
    embed = discord.Embed(title='Here is a dog!', color=random.randint(0, 0xFFFFFF))
    embed.set_image(url=image)
    embed.set_footer(text='by dog.ceo', icon_url='https://i.imgur.com/wJSeh2G.png')
    await ctx.send(embed=embed)

### CAT ###
# Sends a pic of a cat

@bot.command(aliases=['meow', 'kitty', 'getcat'])
async def cat(ctx):
    image = cat_img()
    embed = discord.Embed(title='Here is a cat!', color=random.randint(0, 0xFFFFFF))
    embed.set_image(url=image)
    embed.set_footer(text='by random.cat', icon_url='https://purr.objects-us-east-1.dream.io/static/img/random.cat-logo.png')
    await ctx.send(embed=embed)

### INSPIREME ###
# Sends an inspirational image

@bot.command(aliases=['inspirobot', 'imageinspire'])
async def inspireme(ctx):
    try:
        url = 'http://inspirobot.me/api?generate=true'
        params = {'generate' : 'true'}
        response = requests.get(url, params, timeout=10)
        image = response.text
        embed = discord.Embed(title='An inspirational image...', color=random.randint(0, 0xFFFFFF))
        embed.set_image(url=image)
        embed.set_footer(text='by inspirobot.me', icon_url='https://inspirobot.me/website/images/inspirobot-dark-green.png')
        await ctx.send(embed=embed)
    except RequestException:
        await ctx.send('Inspirobot is broken, there is no reason to live.')


### CHATBOT ###
# summons the cleverbot API to hold a conversation for those who have no life
@bot.command(aliases=['duck', 'db', 'cleverbot', 'r'])
async def duckbot(ctx, *, input):
    response = cleverbotfreeapi.cleverbot(input)
    await ctx.send(response)

### YOUR PING ###
# Tells your ping to the server

@bot.command()
async def ping(ctx):
    await ctx.send("your ping is `" + f'{round (bot.latency * 1000)} ms` ')

##########################
########## TEST ##########
##########################


@bot.command(pass_context=True)
async def name(ctx):
    await ctx.send("{}".format(ctx.message.author.mention))

######### MyID commands
# Test permissons
# test adding reactions


@bot.command()
async def owner(ctx):
    if ctx.message.author.id == ctx.guild.owner_id:
        await ctx.send("{} is the owner of this server".format(ctx.message.author.mention))
    else:
        await ctx.send("{} is not the owner of this server".format(ctx.message.author.mention))

######### Foo command
# idfk why this here

@bot.command()
async def foo(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)

#########
# Role color == embed color

@bot.command()
async def embedcolor(ctx):
    embed = discord.Embed(title='TEST', description='COLOR TEST', color = ctx.me.color)
    await ctx.send(embed=embed)

##############################
##############################
######## HELP COMMAND ########
##############################
##############################

bot.remove_command('help')

@bot.command()
async def help(ctx, argument: typing.Optional[str] = "None"):

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    botprefix = prefixes[str(ctx.guild.id)]

    if (argument == "None"):

        embed = discord.Embed(title='DuckBot help', description=("Hey {}, Here is a list of arguments:".format(ctx.message.author.mention)), color = 0x6c3e82)
        embed.add_field(name='_ _', value='_ _', inline=False)
        embed.add_field(name='help commands', value='Show the list of normal commands', inline=False)
        embed.add_field(name=(botprefix + 'help testing'), value='shows what testing commands do. This list might not be up to date.', inline=False)
        embed.add_field(name=(botprefix + 'help'), value='Gives this message', inline=False)
        embed.add_field(name='_ _', value='_ _', inline=False)
        embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')
        await ctx.send(embed=embed)

    if (argument == "commands"):

        embed = discord.Embed(title='DuckBot help', description=("Hey {}, Here is a list of available commands:".format(ctx.message.author.mention)), color = 0x6c3e82)
        embed.add_field(name='_ _', value='_ _', inline=False)
        embed.add_field(name=(botprefix + 'dog'), value='Gets a random picture of a dog', inline=False)
        embed.add_field(name=(botprefix + 'cat'), value='Gets a random picture of a cat', inline=False)
        embed.add_field(name=(botprefix + 'motivateme'), value='Sends an affirmation', inline=False)
        embed.add_field(name=(botprefix + 'inspireme'), value='Returns an AI generated image from Inspirobot.me', inline=False)
        embed.add_field(name=(botprefix + 'ping'), value="Shwos the bot's ping to the server", inline=False)
        embed.add_field(name=(botprefix + 'setprefix'), value='Changes the prefix of the bot', inline=False)
        embed.add_field(name=(botprefix + 'help'), value='Gives a list of arguments', inline=False)
        embed.add_field(name='_ _', value='_ _', inline=False)
        embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')
        await ctx.send(embed=embed)

    if (argument == "testing"):

        embed = discord.Embed(title='DuckBot help', description=("Hey {}, Here is a list of beta/testing commands. These might not work.".format(ctx.message.author.mention)), color = 0x6c3e82)
        embed.add_field(name='_ _', value='_ _', inline=False)
        embed.add_field(name=(botprefix + 'owner'), value='Testing permissons for an owner-only command and adding reactions to the original command', inline=False)
        embed.add_field(name=(botprefix + 'name'), value='Testing on how to send a mention', inline=False)
        embed.add_field(name=(botprefix + 'foo'), value="Testing on how arguments work", inline=False)
        embed.add_field(name=(botprefix + 'embedcolor'), value="Testing embed color = top role color", inline=False)
        embed.add_field(name=(botprefix + 'help | .help <arg>'), value='Testing argument categories and optional arguments', inline=False)
        embed.add_field(name=(botprefix + 'help'), value='Gives a list of arguments', inline=False)
        embed.add_field(name='_ _', value='_ _', inline=False)
        embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')
        await ctx.send(embed=embed)

    if (argument != "None" and argument != "testing" and argument != "commands"):

        embed = discord.Embed(title='DuckBot help', description='Incorrect argument. type `.help` for a list of available arguments', color = 0x6c3e82)
        await ctx.send(embed=embed)






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
