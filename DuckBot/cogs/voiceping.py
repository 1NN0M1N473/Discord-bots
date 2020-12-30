import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            if after.channel.id == 787743717393563698:
                textchannel = self.bot.get_channel(788226503422902343)
                await textchannel.send('Hey <@349373972103561218>, Someone joined a voice channel!')

def setup(bot):
    bot.add_cog(help(bot))
