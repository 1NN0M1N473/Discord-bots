import discord
import typing
from discord.ext import commands

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, argument: typing.Optional[str] = "None"):
        if (argument == "None"):

            embed = discord.Embed(title='RoboNom help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0xf08136)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.add_field(name='Bot Prefix:', value='_ _ **rn?** _ _ or mention the bot with a message to converse with it.', inline=False)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.add_field(name='rn?help', value='Displays this help screen', inline=False)
            embed.add_field(name='rn?help fun', value='Shows the fun commands you can run', inline=False)
            embed.add_field(name='rn?help commands', value='Shows assorted utility commands')
            embed.add_field(name='rn?help admin', value='Shows administrative commands for the bot backend; most of these can only be run by the creator.', inline=False)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')
            await ctx.send(embed=embed)

        elif(argument == "fun"):

            embed = discord.Embed(title='RoboNom help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0xf08136)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.add_field(name='rn?help', value='Displays usable commands', inline=False)
            embed.add_field(name='rn?quote', value='Fetches a random quote from the ZenQuote API', inline=False)
            embed.add_field(name='rn?nerdyquote', value="Fetches a random programming-themed quote", inline=False)
            embed.add_field(name='rn?robonom <say something>', value="Engage in conversation with the bot; responses not guaranteed to make sense. Can also be used just by mentioning the bot with a message.", inline=False)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')
            await ctx.send(embed=embed)

        elif(argument == "commands"):
            embed = discord.Embed(title='Robonom help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0xf08136)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.add_field(name='rn?ping', value='Measures your latency!', inline=True)
            embed.add_field(name='rn?google <search query', value="Returns the number one Google search result for a given query. Dorking parameters can break it, although they sometimes work :P", inline=True)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')
            await ctx.send(embed=embed)
        elif(argument == "admin"):

            embed = discord.Embed(title='RoboNom help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0xf08136)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.add_field(name='rn?load <module>', value='Forces a cog to load, if it was unloaded or didn\'t load on startup', inline=False)
            embed.add_field(name='rn?unload <module>', value='Forces a cog to unload. The bot will no longer be able to use commands within the cog.', inline=False)
            embed.add_field(name='rn?reload <module>', value='Forces a module to unload and reload, useful for integrating backend changes without restarting the bot.', inline=False)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title='Command Not Found', description='That command or subcommand doesn\'t exist. Do rn?help to see the available commands.', color = 0xFF0000)
            await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(help(bot))
