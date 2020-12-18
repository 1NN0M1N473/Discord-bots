#My first discord bot
#bear with me, code will be crude and probably stupid
#I'm just learning shit

#import libraries

import os
import requests
import json
import discord
import cleverbotfreeapi
import random
from discord.ext import commands
from dotenv import load_dotenv


#client for events, bot for commands
bot = commands.Bot(command_prefix='?')
#cb = cleverbot.CleverBot()

#Create more secure function so I can push to GitHub without compromising the token
#remember to add this in .gitignore

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


#functions

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return(quote)

#initial event configuration

@bot.event
async def on_ready():
    print("Bot is online and ready to go!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='?help'))

#bot commands here

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round (bot.latency * 1000)}ms ')

@bot.command()
async def inspireme(ctx):
    responses = open('jokes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

@bot.command()
async def helpme(ctx):
    await ctx.send("Calling FBI")

@bot.command()
async def beeattack(ctx):
    await ctx.send("https://media.giphy.com/media/yIXVnzpoNiE0w/giphy.gif")

@bot.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

@bot.command()
async def barry(ctx, *, input):
    response = cleverbotfreeapi.cleverbot(input)
    await ctx.send(response)

#bot events here


#@bot.event
#async def on_member_join(member):
#    await member.create_dm()
#    await member.dm_channel.send(
#	f'Hi {member.name}, welcome to the server!'
#    )
"""
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    syscraft_roast = [
	'I eat Syscraft for breakfast',
	'We don\'t say that name here',
	'Who\'s this syscraft person?',
	'I\'ll kill a syscraft. I ain\'t saying I have, and I  ain\'t saying I haven\'t.',
	'Barry > Syscraft'
    ]

    if message.content == 'syscraft':
        response = random.choice(syscraft_roast)
        await message.channel.send(response)
"""
bot.run(TOKEN)
