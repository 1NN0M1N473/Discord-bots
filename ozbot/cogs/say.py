import discord, asyncio, typing
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ##### .s command ####
    # resends the message as the bot

    @commands.command(aliases=['s', 'send', 'foo'])
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        if ctx.channel.permissions_for(ctx.author).mention_everyone:
            if ctx.message.reference:
                reply = ctx.message.reference.resolved
                await reply.reply(msg)
            else:
                await ctx.send(msg)
        else:
            if ctx.message.reference:
                reply = ctx.message.reference.resolved
                await reply.reply(msg, allowed_mentions = discord.AllowedMentions(everyone = False))
            else:
                await ctx.send(msg, allowed_mentions = discord.AllowedMentions(everyone = False))

    @commands.command(aliases=['a', 'an'])
    @commands.has_permissions(manage_messages=True)
    async def announce(self, ctx, channel: typing.Optional[discord.TextChannel] = None, *, msg = "no content"):
        if channel == None:
            await ctx.send("""You must specify a channel
`.announce #channel/ID Message`""")
            return
        await ctx.message.delete()
        if channel.permissions_for(ctx.author).mention_everyone:
            if ctx.message.reference:
                msg = ctx.message.reference.resolved.content
            await channel.send(msg)

        else:
            if ctx.message.reference:
                msg = ctx.message.reference.resolved.content
            await channel.send(msg, allowed_mentions = discord.AllowedMentions(everyone = False))


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def jvc(self, ctx, channel: typing.Optional[discord.VoiceChannel] = None):
        try:
            await channel.connect()
        except:
            pass

    @jvc.error
    async def info_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.add_reaction('🚫')

def setup(bot):
    bot.add_cog(help(bot))
