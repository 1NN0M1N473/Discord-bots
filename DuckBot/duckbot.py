#Leo's first discord bot

#import libraries

import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='.')

#initial event configuration

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/accountname"))
    print('test lol')

@bot.event
async def on_ready():
    print ("Bot Onine!")
    print ("Hello I Am " + bot.user.name)

@bot.command()
async def ping(ctx):
    await ctx.send("the ping is " + f'{round (bot.latency * 1000)} ms ')

@bot.command()
async def horse(ctx):
    await ctx.send("https://media.discordapp.net/attachments/760191301894275113/788301744353312798/image0.jpg")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

bot.run('Nzg4Mjc4NDY0NDc0MTIwMjAy.X9hLhw.o8eEZy7UPO8J4_G0LYHkFYEV1jE')
