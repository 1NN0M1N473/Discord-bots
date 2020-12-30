import os, discord, asyncio
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default() # Enable all intents except for members and presences
intents.members = True  # Subscribe to the privileged members intent.

bot = commands.Bot(command_prefix=commands.when_mentioned_or('.', 'duck.', 'duckbot.', 'd.', 'du.', 'db.'), case_insensitive=True, intents=intents)


bot.remove_command("help")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print ("Bot Online!")
    print ("Hello I Am " + bot.user.name)
    print ('-----------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='.help'))

@bot.command()
@commands.guild_only()
async def load(ctx, extension):
    if ctx.message.author.id == 349373972103561218:
        bot.load_extension("cogs.{}".format(extension))
        await ctx.message.add_reaction("✅")
        await asyncio.sleep(10)
        await ctx.message.delete()
    else:
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(5)
        await ctx.message.delete()

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("❌")
        await asyncio.sleep(10)
        await ctx.message.delete()

@bot.command()
@commands.guild_only()
async def unload(ctx, extension):
    if ctx.message.author.id == 349373972103561218:
        bot.unload_extension("cogs.{}".format(extension))
        await ctx.message.add_reaction("✅")
        await asyncio.sleep(10)
        await ctx.message.delete()
    else:
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(5)
        await ctx.message.delete()

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("❌")
        await asyncio.sleep(10)
        await ctx.message.delete()

@bot.command()
@commands.guild_only()
async def reload(ctx, extension):
    if ctx.message.author.id == 349373972103561218:
        bot.unload_extension("cogs.{}".format(extension))
        bot.load_extension("cogs.{}".format(extension))
        await ctx.message.add_reaction("✅")
        await asyncio.sleep(10)
        await ctx.message.delete()
    else:
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(5)
        await ctx.message.delete()

@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("❌")
        await asyncio.sleep(10)
        await ctx.message.delete()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension("cogs.{}".format(filename[:-3]))


bot.run(TOKEN, reconnect=True)
