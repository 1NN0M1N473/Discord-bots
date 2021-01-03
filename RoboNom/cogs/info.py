import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title='Information about RoboNom', description="Here's some information about me", color = 0xf08136)
        embed.add_field(name='_ _', value='_ _', inline=False)
        embed.add_field(name='Creator', value='1NN0M1N473#1337', inline=False)
        embed.add_field(name='Server count', value="I'm in " + f'{len(self.bot.guilds)}' + " servers!", inline=False)
        embed.add_field(name='GitHub', value='[Click here](https://github.com/1NN0M1N473/Discord-bots/tree/master/RoboNom) to see my source code!')
        embed.add_field(name='Invite', value='[Click here](https://discord.com/api/oauth2/authorize?client_id=788139657711452190&permissions=2117991635&scope=bot) to invite me to your server!', inline=False)
        embed.add_field(name='Support Server', value='[Click here](https://discord.com/invite/CD2UfNhSev) to join my support server!', inline=False)
        embed.add_field(name='_ _', value='[Bots.gg Listing](https://discord.bots.gg/bots/788139657711452190)', inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
