import typing, discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['pm', 'md', 'message', 'direct'])
    async def dm(self, ctx, id: typing.Optional[int], *, message = ""):
        if ctx.message.author.id == 349373972103561218:
            if id == None:
                await ctx.message.add_reaction('🔢')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return
            if len(f'{id}') != 18:
                await ctx.message.add_reaction('#️⃣')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return
            member = self.bot.get_user(id)
            channel = self.bot.get_channel(795060599666114591)
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass
            try:
                if ctx.message.attachments:
                    file = ctx.message.attachments[0]
                    myfile = await file.to_file()
                    await member.send(message, file=myfile)
                    embed = discord.Embed(color=0x47B781)
                    embed.add_field(name=f'<:outgoingarrow:797567337976430632> **{member.name}#{member.discriminator}**', value=message)
                    embed.set_footer(text=f'.dm {member.id}')
                    await channel.send(embed=embed, file=myfile)
                else:
                    await member.send(message)
                    embed = discord.Embed(color=0x47B781)
                    embed.add_field(name=f'<:outgoingarrow:797567337976430632> **{member.name}#{member.discriminator}**', value=message)
                    embed.set_footer(text=f'.dm {member.id}')
                    await channel.send(embed=embed)
            except discord.Forbidden:
                await ctx.send(f"{member}'s DMs are closed.")
        else:
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep (5)
            await ctx.message.delete()

    @dm.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep (5)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
