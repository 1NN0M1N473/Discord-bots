# COMMAND NOT AVAILABLE!!!
# THIS IS ONLY FOR MEMBERS OF A SPECIFIC GUILD

import typing, discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['sn', 'nick'])
    async def setnick(self, ctx, member : discord.Member, *, new : typing.Optional[str] = 'a'):
        old = f'{ctx.author.nick}'
        if old == 'None':
            old = f'{ctx.author.name}'
        else:
            old = old
        if ctx.guild.id == 787743716793516062:
            try:
                await member.edit(nick=new)
            except discord.Forbidden:
                await ctx.message.add_reaction('⛔')
                return
            except discord.HTTPException:
                await ctx.message.add_reaction('#️⃣')
                await ctx.message.add_reaction('3️⃣')
                await ctx.message.add_reaction('2️⃣')
                return
            await ctx.message.delete()
            channel = self.bot.get_channel(795806295197876275)
            await channel.send(f"""__**📜 NICK LOG 📜**__ __{ctx.author.mention}__ edited __**{member}**__
**`{old}`** -> **`{new}`**""")
        elif member == ctx.author:
            try:
                await member.edit(nick=new)
                await ctx.send(f"""✏ {ctx.author.mention} nick for {member}
**`{old}`** -> **`{new}`**""")
            except discord.Forbidden:
                await ctx.send(f'🚫 Bot not high enough in role hierarchy 🚫', delete_after=15)
                return
            except discord.HTTPException:
                await ctx.message.add_reaction('#️⃣')
                await ctx.message.add_reaction('3️⃣')
                await ctx.message.add_reaction('2️⃣')
                return
###########################################
###########################################
###########################################
        elif ctx.channel.permissions_for(ctx.author).manage_nicknames:
            if member.top_role >= ctx.author.top_role:
                await ctx.send("⚠ Cannot edit nick for members equal or above yourself!")
                return
            try:
                await member.edit(nick=new)
            except discord.Forbidden:
                await ctx.send(f'🚫 Bot not high enough in role hierarchy 🚫', delete_after=15)
                return
            except discord.HTTPException:
                await ctx.message.add_reaction('#️⃣')
                await ctx.message.add_reaction('3️⃣')
                await ctx.message.add_reaction('2️⃣')
        else:
            await ctx.message.add_reaction('🚫')
            return

def setup(bot):
    bot.add_cog(help(bot))
