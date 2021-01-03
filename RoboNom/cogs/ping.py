
import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        pong = f'**{round (self.bot.latency * 1000)}ms **'
        embed = discord.Embed(title='Your Latency:', description=pong, color = 0xf08136, inline=False)
        embed.set_footer(text='Ping is measured as the time in milliseconds it takes a packet to travel from your device to the server.', icon_url='https://i.imgur.com/UNHTZUi.png')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))
