import json, random, discord, requests, typing
from random import randint
from discord.ext import commands


class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uuid(self, ctx, *, argument: typing.Optional[str] = ''):
        response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{argument}")

        embed = discord.Embed(title='Minecraft UUID', color = ctx.me.color)

        if response.status_code == 204:
            embed.add_field(name='⛔ ERROR ⛔', value="There's no player with that name!")

        elif response.status_code == 400:
            embed.add_field(name="⛔ ERROR ⛔", value="ERROR 400! Bad request.")
        else:
            json_data = json.loads(response.text)
            user = json_data["name"]
            uuid = json_data["id"]

            embed.add_field(name=f'Name: `{user}`', value=f"**UUID:** `{uuid}`")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
