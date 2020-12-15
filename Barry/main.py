#My first discord bot
#bear with me, code will be crude and probably stupid
#I'm just learning shit

#import libraries

import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='?')


#Create more secure function so I can push to GitHub without compromising the token

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#initial event configuration

@bot.event
async def on_ready():
    print("Bot is online and ready to go!")

@bot.command()
async def hello(ctx):
    await ctx.send("Now someone remind me how this works exactly?")

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

bot.run(TOKEN)
