import json, random, discord, aiohttp, typing, asyncio
from random import randint
from discord.ext import commands


class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uuid(self, ctx, *, argument: typing.Optional[str] = ''):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.mojang.com/users/profiles/minecraft/{argument}") as cs:
                embed = discord.Embed(color = ctx.me.color)
                if cs.status == 204:
                    embed.add_field(name='⚠ ERROR ⚠', value=f"`{argument}` is not a minecraft username!")

                elif cs.status == 400:
                    embed.add_field(name="⛔ ERROR ⛔", value="ERROR 400! Bad request.")
                else:
                    res = await cs.json()
                    user = res["name"]
                    uuid = res["id"]
                    embed.add_field(name=f'Minecraft username: `{user}`', value=f"**UUID:** `{uuid}`")

                await ctx.send(embed=embed)


    @commands.command(aliases=['w', 'wh'])
    async def whitelist(self, ctx, *, argument: typing.Optional[str] = None):
        user = ctx.guild.get_member(799749818062077962)
        if argument == None:
            await ctx.send("To get whitelisted, run the `.whitelist YourMinecrftName` in the <#706842001135370300> channel. After that, your request will be sent to the staff team. You will get notified trough a DM once you have been whitelisted.")
            return
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.mojang.com/users/profiles/minecraft/{argument}") as cs:
                if cs.status == 204:
                    embed = discord.Embed(color = 0xFF2014)
                    embed.add_field(name='⚠ WHITELISTING ERROR ⚠', value=f"`{argument}` is not a minecraft username!")
                elif cs.status == 400:
                    embed = discord.Embed(color = 0xFF2014)
                    embed.add_field(name='⚠ WHITELISTING ERROR ⚠', value=f"`{argument}` is not a minecraft username!")
                    """
                    elif user.status == discord.Status.online:
                    res = await cs.json()
                    user = res["name"]
                    uuid = res["id"]
                    channel = self.bot.get_channel(764631105097170974)
                    await channel.send(f'whitelist add {user}')
                    channel = self.bot.get_channel(799741426886901850)
                    embed2 = discord.Embed(title='', description=f"Automatically added user `{user}` to the whitelist", color = 0x75AF54)
                    embed2.set_footer(text=f'''{uuid}
requested by: {ctx.author.name}#{ctx.author.discriminator} | {ctx.author.id}''')
                    await channel.send(embed=embed2)
                    embed = discord.Embed(color = 0x75AF54)
                    embed.add_field(name=f'✅ YOU HAVE BEEN WHITELISTED', value=f"Your username `{user}` has been automatically whitelisted!")
                    """
                else:
                    res = await cs.json()
                    user = res["name"]
                    uuid = res["id"]
                    channel = self.bot.get_channel(799741426886901850)
                    embed2 = discord.Embed(title='', description=f"{ctx.author.name}#{ctx.author.discriminator} added whitelist request for `{user}`", color = 0xF3DD53)
                    embed2.set_footer(text=f'.added {ctx.author.id}')
                    await channel.send(embed=embed2)
                    embed = discord.Embed(color = 0x75AF54)
                    embed.add_field(name=f'''✅ Whitelist request for user `{user}` added successfully!''', value=f"You will get notified once you've been whitelisted by a staff member")
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def added(self, ctx, member: typing.Optional[discord.Member]):
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
            embed = discord.Embed(color=0x00FF00)
            embed.add_field(name='OZ-smp whitelisting',value="✅ you have been successfully whitelisted!")
            await member.send(embed=embed)
            embed = discord.Embed(title=f'✅ **{member.name}#{member.discriminator}** whitelisted', color=0x00FF00)
            await channel.send(embed=embed)
        except discord.Forbidden:
            await ctx.send(f"{member}'s DMs are closed.")

def setup(bot):
    bot.add_cog(help(bot))
