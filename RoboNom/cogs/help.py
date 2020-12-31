import os
import json
import random
import typing
import discord
import requests
import asyncio
import cleverbotfreeapi
import discord.client
import discord.channel
from random import randint
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from requests.exceptions import RequestException

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def help(ctx, argument: typing.Optional[str] = "None"):

    if (argument == "None"):
        embed = discord.Embed(title='Barry help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0x00FFFF)
        embed.add_field(name='_ _', value='_ _', inline=False)
        embed.add_field(name='?help commands', value='Shows the commands you can run. Currently the only argument, more to come!', inline=False)
        embed.add_field(name='?help', value='Displays this help screen', inline=False)
        embed.add_field(name='Work in Progress', value='This help screen is consistently being updated with new commands, and will change significantly when I finish integrating cogs.')
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
            embed.add_field(name='?barry <say something>', value="Engage in conversation with the bot; responses not guaranteed to make sense", inline=False)
            embed.add_field(name='?google <search query', value="Returns the number one Google search result for a given query. Can also use dorking parameters like site: and inurl:")
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')
            await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title='Barry help', description='No command found. What exactly are you trying to accomplish? Run ?help again.', color = 0xFF0000)
        embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))
