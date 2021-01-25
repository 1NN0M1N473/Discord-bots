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
                try: await ctx.message.delete()
                except discord.Forbidden: pass

            if type == "playing":
                if argument !=  "2e3af8c32eb727e22f076be964574181":
                    # Setting `Playing ` status
                    await self.bot.change_presence(activity=discord.Game(name=f'{argument}'))
                    await ctx.message.add_reaction('✅')
                    await ctx.send(f"Activity changed to `Playing {argument}` ", delete_after=10)
                    await asyncio.sleep(10)
                    try:
                        await ctx.message.delete()
                    except discord.Forbidden:
                        pass

            if type == "listening":
                if argument !=  "2e3af8c32eb727e22f076be964574181":
                    # Setting `Listening ` status
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{argument}'))
                    await ctx.message.add_reaction('✅')
                    await ctx.send(f"Activity changed to `Listening to {argument}` ", delete_after=10)
                    await asyncio.sleep(10)
                    try: await ctx.message.delete()
                    except discord.Forbidden: pass

            if type == "watching":
                if argument !=  "2e3af8c32eb727e22f076be964574181":
                    #Setting `Watching ` status
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{argument}'))
                    await ctx.message.add_reaction('✅')
                    await ctx.send(f"Activity changed to `Watching {argument}` ", delete_after=10)
                    await asyncio.sleep(10)
                    try: await ctx.message.delete()
                    except discord.Forbidden: pass

            if type == "competing":
                if argument !=  "2e3af8c32eb727e22f076be964574181":
                    #Setting `other ` status
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f'{argument}'))
                    await ctx.message.add_reaction('✅')
                    await ctx.send(f"Activity changed to `Competing in {argument}` ", delete_after=10)
                    await asyncio.sleep(10)
                    try: await ctx.message.delete()
                    except discord.Forbidden: pass

            if type == "clear":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name='cleared'))
                await ctx.message.add_reaction('✅')
                await ctx.send(f"Activity cleared ", delete_after=10)
                await asyncio.sleep(10)
                try: await ctx.message.delete()
                except discord.Forbidden: pass

            if type != "watching" and type != "listening" and type != "playing" and type != "competing" and type != "clear" and type != "4afc07a4055edc68da62f18f7ecdd103":
                embed = discord.Embed(title= "`ERROR` INVALID TYPE!", description="Here is a list of available types:", color = ctx.me.color)
                embed.add_field(name=(botprefix + 'status Playing <status>'), value='Sets the status to Playing.', inline=False)
                embed.add_field(name=(botprefix + 'status Listening <status>'), value='Sets the status to `Listening to`.', inline=False)
                embed.add_field(name=(botprefix + 'status Watching <status>'), value='Sets the status to `Watching`.', inline=False)
                embed.add_field(name=(botprefix + 'status Competing <status>'), value='Sets the status to `Competing in`.', inline=False)
                await ctx.send(embed=embed, delete_after=45)
                await asyncio.sleep(45)
                try: await ctx.message.delete()
                except discord.Forbidden: pass
        else:
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep(5)
            try: await ctx.message.delete()
            except discord.Forbidden: pass



    @commands.command(aliases = ['stop','sd'])
    async def shutdown(self, ctx):
        if ctx.message.author.id == 349373972103561218:
            guild = self.bot.get_guild(787743716793516062)
            try:
                await guild.voice_client.disconnect()
            except AttributeError:
                a=1
            await ctx.send("🛑 **__Stopping the bot__**")
            await ctx.bot.logout()
        else:
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep(5)
            try: await ctx.message.delete()
            except discord.Forbidden: pass

    @commands.command()
    async def todo(self, ctx, *, message = None):
        if ctx.message.author.id != 349373972103561218:
            await ctx.message.add_reaction('🚫')
            return
        channel = self.bot.get_channel(799211271542145034)
        if message == None:
            await ctx.message.add_reaction('⚠')
            return
        if ctx.message.channel == channel:
            await ctx.message.delete()
        embed = discord.Embed(description=message, color=0x47B781)
        await channel.send(embed=embed)
        await ctx.message.add_reaction('✅')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            if after.channel.id == 787743717393563698:
                textchannel = self.bot.get_channel(788226503422902343)
                await textchannel.send('Hey <@349373972103561218>, Someone joined a voice channel!')

def setup(bot):
    bot.add_cog(help(bot))
