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

    #pings you

    @commands.command(pass_context=True)
    async def name(self, ctx):
        await ctx.send("{}".format(ctx.message.author.mention))

    # Checks if you're the owner

    @commands.command()
    async def owner(self, ctx):
        if ctx.message.author.id == ctx.guild.owner_id:
            await ctx.send("{} is the owner of this server".format(ctx.message.author.mention))
        else:
            await ctx.send("{} is not the owner of this server".format(ctx.message.author.mention))

    #########
    # Role color == embed color

    @commands.command()
    async def embedcolor(self, ctx):
        embed = discord.Embed(title='TEST', description='COLOR TEST', color = ctx.me.color)
        await ctx.send(embed=embed)

    ######### test commands
    # Test permissons
    # test adding reactions

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def test(self, ctx):
        await ctx.send('you are an admin :white_check_mark:')

    @test.error
    async def test_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction('🚫')

def setup(bot):
    bot.add_cog(help(bot))
