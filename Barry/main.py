#My first discord bot
#bear with me, code will be crude and probably stupid
#I'm just learning shit

#import libraries

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

#initial event configuration

@bot.event
async def on_ready():
    print("Rawwwwrrrr")

@bot.command()
async def hello(ctx):
    await ctx.send("Now someone remind me how this works exactly?")



bot.run('<insert token>')
