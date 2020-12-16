#DUCKBOT.
#This bot is probably not the best as it is my first one. i'm sorry lol.
#All the stuff here was learnt along the way with no previous experience

#import libraries

import os
import discord
import random
from random import randint
import discord.channel 
import discord.client
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
import requests
from requests.exceptions import RequestException

bot = commands.Bot(command_prefix='.')

#GITHUB TOKEN THINGY

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

###### INITIAL CONFIG #####

@bot.event
async def on_ready():
    print ("Bot Onine!")
    print ("Hello I Am " + bot.user.name)
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

### TEST ###

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 787743717393563698:
            channel = bot.get_channel(788226503422902343)
            await client.send_message(message.channel, content = "Hello!")



#######################
##### HELP COMMAND ####
#######################

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='DuckBot help', description='Here is a list of available commands:', color = 0x6c3e82)
    embed.add_field(name='.horse', value='Requested by Fel - Shows an old photo of Fel.', inline=False)
    embed.add_field(name='.inspireme', value='Returns an AI generated image from Inspirobot.me', inline=False)
    embed.add_field(name='.ping', value="Shwos the bot's ping to the server", inline=False)
    embed.add_field(name='.help', value='Gives this message', inline=False)
    embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')

    await ctx.send(embed=embed)

bot.run(TOKEN)
