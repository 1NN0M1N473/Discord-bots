import discord
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

def setup(bot):
    bot.add_cog(ModMail(bot))
