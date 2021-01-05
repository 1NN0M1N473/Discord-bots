import json, random, typing, discord, asyncio
from random import randint
from dotenv import load_dotenv
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx, argument: typing.Optional[str] = "None", number: typing.Optional[int] = 1):

        botprefix = '.'

        if (argument == "None"):

            embed = discord.Embed(title='DuckBot help', description=("""Hey {}, Here is a list of commands:
fields: `<obligatory>` `[optional]`""".format(ctx.message.author.mention)), color = ctx.me.color)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.add_field(name=botprefix + 'help commands', value='Show normal commands', inline=True)
            embed.add_field(name=(botprefix + 'help testing'), value='shows testing/beta commands.', inline=True)
            embed.add_field(name=(botprefix + 'help moderation'), value='shows moderation commands.', inline=True)
            embed.add_field(name=(botprefix + 'info'), value='Gives info about the bot, and how to get support.', inline=True)
            embed.add_field(name=(botprefix + 'help [argument] [page]'), value='Gives this message or the other sub-categories.', inline=True)
            embed.add_field(name=(botprefix + 'log'), value='Gives an update log', inline=True)
            embed.add_field(name='_ _', value=':sparkles: Fixed infite for the [support server](https://discord.gg/gRAUH8n9nV):sparkles:', inline=False)
            embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')
            await ctx.send(embed=embed, delete_after=100)
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                return
            return

        if (argument == "commands"):

            embed = discord.Embed(title='DuckBot help', description=("Hey {}, Here is a list normal/fun commands.".format(ctx.message.author.mention)), color = ctx.me.color)
            if number == 1:

                embed.add_field(name=(botprefix + 'dog'), value='Gets a random picture of a dog', inline=False)
                embed.add_field(name=(botprefix + 'cat'), value='Gets a random picture of a cat', inline=False)
                embed.add_field(name=(botprefix + 'motivateme'), value='Sends an affirmation', inline=False)
                embed.add_field(name=(botprefix + 'inspireme'), value='Returns an AI generated image from Inspirobot.me', inline=False)
                embed.add_field(name=(botprefix + 'ping'), value="Shwos the bot's ping to the server", inline=False)

            if number == 2:

                embed.add_field(name=(botprefix + 'help'), value='Gives a list of arguments', inline=False)
                embed.add_field(name=(botprefix + 'afk'), value='Sets/unsets you as AFK. (adds `[AFK]` to your nickname)', inline=False)
                embed.add_field(name=(botprefix + 'say'), value="Testing on how arguments work `perm requiered = manage messages`", inline=False)

            embed.add_field(name='_ _', value=f'Help commands | page `{number}/2`', inline=False)
            embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')
            await ctx.send(embed=embed, delete_after=100)
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                return
            return

        if (argument == "testing"):

            embed = discord.Embed(title='DuckBot help', description=("Hey {}, Here is a list of beta/testing commands. These might not work.".format(ctx.message.author.mention)), color = ctx.me.color)
            embed.add_field(name='_ _', value='_ _', inline=False)

            if number == 1:
                embed.add_field(name=(botprefix + 'uuid <player>'), value='[MINECRAFT] Gives the UUID of a given player - NOT WORKING', inline=False)

            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.add_field(name='_ _', value=f'Help commands | page `{number}/1`', inline=False)
            embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')
            await ctx.send(embed=embed, delete_after=100)
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                return
            return

        if (argument == "moderation"):

            embed = discord.Embed(title='DuckBot help', description=("Hey {}, Here is a list of beta/testing commands. These might not work.".format(ctx.message.author.mention)), color = ctx.me.color)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.add_field(name=(botprefix + 'purge'), value='Purges messages in a channel. Limit = 1000 messages.', inline=False)
            embed.add_field(name=(botprefix + 'kick'), value='kicks a member.', inline=False)
            embed.add_field(name=(botprefix + 'ban'), value='bans a member.', inline=False)
            embed.add_field(name='_ _', value='_ _', inline=False)
            embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')
            await ctx.send(embed=embed, delete_after=100)
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                return
            return

        if (argument == "owner"):
            if ctx.message.author.id == 349373972103561218:
                embed = discord.Embed(title='BOT MANAGEMENT COMMANDS', description=("Hey {}, Here are administration commands.".format(ctx.message.author.mention)), color = ctx.me.color)
                embed.add_field(name='_ _', value='_ _', inline=False)
                embed.add_field(name=(botprefix + 'load <cog>'), value='Loads a cog.', inline=False)
                embed.add_field(name=(botprefix + 'unload <cog>'), value='Unloads a cog.', inline=False)
                embed.add_field(name=(botprefix + 'reload <cog>'), value='Reloads a cog.', inline=False)
                embed.add_field(name=(botprefix + 'setstatus'), value='Sets the status of the bot.', inline=False)
                embed.add_field(name=(botprefix + 'shutdown'), value='Shuts down the bot.', inline=False)
                embed.add_field(name=(botprefix + 'edit <msgID> <new message> <tag>'), value="""Edits a bot't message
**tags:** `--s` removes embed. `--d` deletes content.""", inline=False)
                embed.add_field(name='_ _', value='_ _', inline=False)
                embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')
                await ctx.send(embed=embed, delete_after=100)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return
            else:
                embed = discord.Embed(title='DuckBot error', description=("Hey {}, You are not allowed to run this command!".format(ctx.message.author.mention)), color = ctx.me.color)
                embed.set_footer(text='Bot by LeoCx1000#9999', icon_url='https://i.imgur.com/DTLCaur.gif')
                await ctx.message.delete()
                await ctx.send(embed=embed, delete_after=100)

        if (argument != "None" and argument != "testing" and argument != "commands" and argument != "moderation" and argument != "owner"):

            embed = discord.Embed(title='DuckBot help', description='Incorrect argument. type `.help` for a list of available arguments', color = ctx.me.color)
            await ctx.send(embed=embed, delete_after=100)
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                return
            return

def setup(bot):
    bot.add_cog(help(bot))
