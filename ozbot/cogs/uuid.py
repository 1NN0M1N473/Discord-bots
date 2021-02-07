import json, random, discord, aiohttp, typing
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
    async def whitelist(self, ctx, *, argument: typing.Optional[str] = ''):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.mojang.com/users/profiles/minecraft/{argument}") as cs:
                if cs.status == 204:
                    embed = discord.Embed(color = 0xFF2014)
                    embed.add_field(name='⚠ WHITELISTING ERROR ⚠', value=f"`{argument}` is not a minecraft username!")

                elif cs.status == 400:
                    embed = discord.Embed(color = 0xFF2014)
                    embed.add_field(name='⚠ WHITELISTING ERROR ⚠', value=f"`{argument}` is not a minecraft username!")
                else:
                    res = await cs.json()
                    user = res["name"]
                    uuid = res["id"]
                    channel = self.bot.get_channel(799741426886901850)
                    embed2 = discord.Embed(title='', description=f"{ctx.author.name}#{ctx.author.discriminator} added whitelist request for `{user}`", color = 0xF3DD53)
                    embed2.set_footer(text=f'.added {ctx.author.id}')
                    await channel.send(embed=embed2)
                    embed = discord.Embed(color = 0x75AF54)
                    embed.add_field(name=f'✅ Request added for the name `{user}`', value=f"You will get notified once you've been added to the server")
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def added(self, ctx, member: typing.Optional[discord.Member]):
        await ctx.send(".added not working rn lol")
        return
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

def setup(bot):
    bot.add_cog(help(bot))
