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
        channel = self.bot.get_channel(795060599666114591)
        if message.attachments:
            embed = discord.Embed(color= 0xFF0000)
            embed.add_field(name='⛔ ERROR ⛔', value="""Images are currently not supported in DMs.
You can use [imgur](https://imgur.com/upload) to send a images and
[pastebin](https://paste.gg/) to send long text files/messages!

⚠ `this message wasn't delivered!` ⚠
Remove the image/file and resend your message""")
            await message.channel.send(embed=embed)
            return
        else:
            embed = discord.Embed()
            embed.add_field(name=f'**<{message.author} |** `{message.author.id}`**>**', value=f'{message.content}')
            await channel.send(embed=embed)
        await message.add_reaction('📬')
        await asyncio.sleep(2.5)
        await message.remove_reaction('📬', self.bot.user)

def setup(bot):
    bot.add_cog(help(bot))
