# COMMAND NOT AVAILABLE!!!
# THIS IS ONLY FOR MEMBERS OF A SPECIFIC GUILD

import typing, discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['sn', 'nick'])
    async def setnick(self, ctx, member : discord.Member, *, new : typing.Optional[str] = 'None'):
        if new == 'None':
            new = f'{member.name}'
        else:
            new = new
        old = f'{member.nick}'
        if old == 'None':
            old = f'{member.name}'
        else:
            old = old
        if member == ctx.author and ctx.channel.permissions_for(ctx.author).change_nickname:
            try:
                await member.edit(nick=new)
                await ctx.send(f"""✏ {ctx.author.mention} nick for {member}
**`{old}`** -> **`{new}`**""")
                try: await ctx.message.delete()
                except discord.Forbidden: return
            except discord.Forbidden:
                await ctx.send(f'🚫 Bot not high enough in role hierarchy 🚫', delete_after=15)
                return
            except discord.HTTPException:
                await ctx.message.add_reaction('#️⃣')
                await ctx.message.add_reaction('3️⃣')
                await ctx.message.add_reaction('2️⃣')
                return
        elif ctx.channel.permissions_for(ctx.author).manage_nicknames:
            if member.top_role >= ctx.author.top_role:
                await ctx.send("⚠ Cannot edit nick for members equal or above yourself!")
                return
            try:
                await member.edit(nick=new)
                await member.edit(nick=new)
                await ctx.send(f"""✏ {ctx.author.mention} edited nick for **{member}**
**`{old}`** -> **`{new}`**""")
                try: await ctx.message.delete()
                except discord.Forbidden: return
            except discord.Forbidden:
                await ctx.send(f'🚫 Bot not high enough in role hierarchy 🚫', delete_after=15)
                return
            except discord.HTTPException:
                await ctx.message.add_reaction('#️⃣')
                await ctx.message.add_reaction('3️⃣')
                await ctx.message.add_reaction('2️⃣')
        elif member == ctx.author and ctx.channel.permissions_for(ctx.author).change_nickname:
            await ctx.send(f"""🚫 You can only change your own nick!
> .nick {ctx.author.mention} `<new nick>`""", delete_after=15)
            return
        else:
            await ctx.message.add_reaction('🚫')

def setup(bot):
    bot.add_cog(help(bot))
