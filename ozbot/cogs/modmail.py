import discord, asyncio, typing
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild: return
        if message.author == self.bot.user: return
        if message.content.startswith('.'):
            await message.channel.send('⚠ messages starting with `.` will not be sent ⚠')
        channel = self.bot.get_channel(799741426886901850)
        if message.attachments:
            embed = discord.Embed(color= 0xFF0000)
            embed.add_field(title='⛔ ERROR ⛔', value="""Images are currently not supported in DMs.
You can use [imgur](https://imgur.com/upload) to send a images and
[pastebin](https://paste.gg/) to send long text files/messages!

⚠ `this message wasn't delivered!` ⚠
Remove the image/file and resend your message""")
            await message.channel.send(embed=embed)
            return
        else:
            embed = discord.Embed(color=0xD7342A)
            embed.add_field(name=f'<:incomingarrow:797567338320887858> **{message.author}**', value=f'{message.content}')
            embed.set_footer(text=f'.dm {message.author.id}')
            await channel.send(embed=embed)
        await message.add_reaction('📬')
        await asyncio.sleep(2.5)
        await message.remove_reaction('📬', self.bot.user)


    @commands.Cog.listener()
    async def on_member_join(self, member):
       await self.bot.get_channel(706624465378738217).send(f"""{member.mention}, Welcome to {member.guild.name}! Make sure to read and agree to the <#706825075516768297> to get access to the rest of {member.guild.name}.
To get whitelisted, run the `.whitelist YourMinecraftName` command in the <#706842001135370300> channel! """)
       await self.bot.get_channel(708316690638700607).send(f"""<:incomingarrow:800218133225930763> **{member.name}#{member.discriminator}** joined **{member.guild.name}**!""")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
       await self.bot.get_channel(708316690638700607).send(f"""<:outgoingarrow:800218133364867073> **{member.name}#{member.discriminator}** left **{member.guild.name}**!""")

    @commands.command(aliases=['pm', 'md', 'message', 'direct'])
    @commands.has_permissions(manage_messages=True)
    async def dm(self, ctx, member: typing.Optional[discord.Member], *, message = ""):
        if member == None:
            await ctx.message.add_reaction('⁉')
            await asyncio.sleep(5)
            await ctx.message.delete()
            return
        channel = self.bot.get_channel(799741426886901850)
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

    @dm.error
    async def dm_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction('🚫')
            await asyncio.sleep (5)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(help(bot))
