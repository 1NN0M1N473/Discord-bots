import typing, discord, asyncio, json
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        # Don't question the weird numbers. Just there because they're hard to guess.

    @commands.command(aliases = ['setstatus', 'ss', 'activity'])
    async def status(self, ctx, thetype: typing.Optional[str] = "4afc07a4055edc68da62f18f7ecdd103",* , argument: typing.Optional[str] = "2e3af8c32eb727e22f076be964574181"):
        if ctx.message.author.id == 349373972103561218:
            botprefix = '.'
            type = thetype.lower()

            if type == "4afc07a4055edc68da62f18f7ecdd103":
                embed = discord.Embed(title= "`ERROR` NO STATUS GIVEN!", description="Here is a list of available types:", color = ctx.me.color)
                embed.add_field(name=(botprefix + 'status Playing <status>'), value='Sets the status to Playing.', inline=False)
                embed.add_field(name=(botprefix + 'status Listening <status>'), value='Sets the status to Listening.', inline=False)
                embed.add_field(name=(botprefix + 'status Watching <status>'), value='Sets the status to Watching.', inline=False)
                await ctx.send(embed=embed, delete_after=45)
                await asyncio.sleep(45)
                await ctx.message.delete()

            if type == "playing":
                if argument !=  "2e3af8c32eb727e22f076be964574181":
                    # Setting `Playing ` status
                    await self.bot.change_presence(activity=discord.Game(name=f'{argument}'))
                    await ctx.message.add_reaction('✅')
                    await ctx.send(f"Activity changed to `Playing {argument}` ", delete_after=10)
                    await asyncio.sleep(10)
                    await ctx.message.delete()

            if type == "listening":
                if argument !=  "2e3af8c32eb727e22f076be964574181":
                    # Setting `Listening ` status
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{argument}'))
                    await ctx.message.add_reaction('✅')
                    await ctx.send(f"Activity changed to `Listening to {argument}` ", delete_after=10)
                    await asyncio.sleep(10)
                    await ctx.message.delete()

            if type == "watching":
                if argument !=  "2e3af8c32eb727e22f076be964574181":
                    #Setting `Watching ` status
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{argument}'))
                    await ctx.message.add_reaction('✅')
                    await ctx.send(f"Activity changed to `Watching {argument}` ", delete_after=10)
                    await asyncio.sleep(10)
                    await ctx.message.delete()

            if type != "watching" and type != "listening" and type != "playing" and type != "4afc07a4055edc68da62f18f7ecdd103":
                embed = discord.Embed(title= "`ERROR` INVALID TYPE!", description="Here is a list of available types:", color = ctx.me.color)
                embed.add_field(name=(botprefix + 'status Playing <status>'), value='Sets the status to Playing.', inline=False)
                embed.add_field(name=(botprefix + 'status Listening <status>'), value='Sets the status to Listening.', inline=False)
                embed.add_field(name=(botprefix + 'status Watching <status>'), value='Sets the status to Watching.', inline=False)
                await ctx.send(embed=embed, delete_after=45)
                await asyncio.sleep(45)
                await ctx.message.delete()
        else:
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep(5)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
