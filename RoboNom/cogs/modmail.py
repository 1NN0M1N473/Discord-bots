import discord, typing
import asyncio
from discord.ext import commands

class ModMail(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild: return
        if message.author == self.bot.user: return
        if message.content.startswith('rn?'): return
        channel = self.bot.get_channel(795007497995157515)
        if message.attachments:
            embed = discord.Embed(color = 0xFF0000)
            embed.add_field(name='<--[Error]-->', value="""Due to Discord\'s limitations for bots, images aren\'t currently supported in DMs.
If an image is necessary, please upload it to [imgur](https://imgur.com/upload) and
paste the link here. You can also use [pastebin](https://paste.gg) to send extra long messages or snippets.

:warning: `This message wasn't delivered!` :warning:
Please remove the attachments/images and try again.""")

            await message.channel.send(embed=embed)
            return
        else:
            await channel.send('<@645083460658003969>')
            embed = discord.Embed(title='ModMail Alert!', description='_ _', color = 0x00FF00)
            embed.add_field(name=f'**<{message.author} |** `{message.author.id}`**>**', value=f'{message.content}')
            await channel.send(embed=embed)
        await message.add_reaction('📬')

    @commands.command(aliases=['pm', 'md', 'message', 'direct'])
    async def dm(self, ctx, id: typing.Optional[int], *, message = ""):
        if ctx.message.author.id == 645083460658003969:
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

            if member == None:
                await ctx.message.add_reaction('⁉')
                await asyncio.sleep(3)
                try:
                    await ctx.message.delete()
                except discord.Forbidden:
                    return
                return

            channel = self.bot.get_channel(795007497995157515)
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
    bot.add_cog(ModMail(bot))
