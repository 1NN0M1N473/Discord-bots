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
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason: typing.Optional[str] = "No reason specified"):
        if member.top_role < ctx.author.top_role:
            if member.guild_permissions.ban_members == False:
                await member.ban(reason=reason)
                await ctx.send(f"""**{ctx.message.author}** has banned **{member}**!
**Reason:** `{reason}`""")
            else:
                await ctx.send(f"**{ctx.message.author}**, you can't ban another moderator!", delete_after=10)
                await ctx.message.delete()

        else:
            await ctx.send(f"**{member}** is higher than you in role hierarchy!", delete_after=10)
            await asyncio.sleep (2)
            await ctx.message.delete()

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep (2)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
