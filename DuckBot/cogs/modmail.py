import discord, asyncio
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild: return
        if message.author == self.bot.user: return
        if message.content.startswith('.'): return
        channel = self.bot.get_channel(792309722362937344)
        if message.attachments:
            file = message.attachments[0]
            myfile = await file.to_file()
            embed = discord.Embed()
            embed.add_field(name=f'**<{message.author} |** `{message.author.id}`**>**', value=f'{message.content}')
            await channel.send(embed=embed, file=myfile)
        else:
            embed = discord.Embed()
            embed.add_field(name=f'**<{message.author} |** `{message.author.id}`**>**', value=f'{message.content}')
            await channel.send(embed=embed)
        await message.add_reaction('📬')
        await asyncio.sleep(2.5)
        await message.remove_reaction('📬', self.bot.user)

def setup(bot):
    bot.add_cog(help(bot))
