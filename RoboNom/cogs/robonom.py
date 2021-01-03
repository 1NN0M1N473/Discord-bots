import discord
import asyncio
import cleverbotfreeapi
from discord.ext import commands

class RoboNom(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user in message.mentions:
                clever_response = cleverbotfreeapi.cleverbot(message.content)
                await message.channel.send(clever_response)

    @commands.command()
    async def robonom(self, ctx, *, input):
        response = cleverbotfreeapi.cleverbot(input)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(RoboNom(bot))
