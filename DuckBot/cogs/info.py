import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title='DuckBot info', description="Here's information about my bot:", color=ctx.me.color)

        # give info about you here
        embed.add_field(name='Author', value='LeoCx1000#9999', inline=True)

        # Shows the number of servers the bot is member of.
        embed.add_field(name='Server count', value="i'm in " + f'{len(self.bot.guilds)}' + " servers", inline=True)

        # give users a link to invite this bot to their server
        embed.add_field(name='Invite', value='Invite me to your server [here](https://discord.com/api/oauth2/authorize?client_id=788278464474120202&permissions=8&scope=bot)', inline=True)

        embed.add_field(name='Source code', value="[Here](https://github.com/1NN0M1N473/Discord-bots/tree/master/DuckBot)'s my sourcecode", inline=True)

        embed.add_field(name='Support server', value="[Here](https://github.com/1NN0M1N473/Discord-bots/tree/master/DuckBot)'s my sourcecode", inline=True)

        embed.add_field(name='_ _', value='_ _', inline=False)

        embed.add_field(name='Bug report and support:', value= """To give a suggestion and report a bug, typo or issue DM the bot.
`due to discord's limitations, you will not get a response to this DM!`
_ _
For further help, join the :sparkles:[support server](https://discord.gg/ZmQe8gbSzE):sparkles:""", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
