import discord
import asyncio
from discord.ext import commands
from googlesearch import search

class GoogleSearch(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def google(self, ctx, *, query):
        async with ctx.typing():
            author = ctx.author.mention
            result = await ctx.send(f"Finding the number one Google result for that query {author}....")
            for j in search(query, tld="co.in", num=1, stop=1, pause=2):
                print(f"{author} searched for " + query + " and got " + j)
                await result.edit(content=j)

def setup(bot):
    bot.add_cog(GoogleSearch(bot))
