import os, discord, asyncio
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default() # Enable all intents except for members and presences
intents.members = True  # Subscribe to the privileged members intent.
intents.presences = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('.', 'oz.', 'o.'), case_insensitive=True, intents=intents)

bot.load_extension('jishaku')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print("======[ BOT ONLINE! ]======")
    print ("Logged in as " + bot.user.name)
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='support DMs'))



@bot.command()
@commands.guild_only()
async def load(ctx, extension):
    if ctx.message.author.id == 349373972103561218:
        try:
            bot.load_extension("cogs.{}".format(extension))
            await ctx.message.add_reaction("✅")
        except discord.ext.commands.ExtensionAlreadyLoaded:
            await ctx.send("Cog already loaded!", delete_after=5)
        except discord.ext.commands.ExtensionNotFound:
            await ctx.message.add_reaction("❓")
        except discord.ext.commands.NoEntryPointError:
            await ctx.send("Cog doesn't have a setup function!", delete_after=5)
        await asyncio.sleep(5)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return
        except discord.NotFound:
            return
        return
    else:
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(3)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return
        except discord.NotFound:
            return
        return

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("❌")
        await ctx.send(f"""```⚠ {error}
[ℹ] for more information check the console```""")
        await asyncio.sleep(3)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return
        except discord.NotFound:
            return
        return

@bot.command()
@commands.guild_only()
async def unload(ctx, extension):
    if ctx.message.author.id == 349373972103561218:
        try:
            bot.unload_extension("cogs.{}".format(extension))
            await ctx.message.add_reaction("✅")
        except discord.ext.commands.ExtensionNotLoaded:
            await ctx.send("Cog wasn't loaded!", delete_after=5)
        await asyncio.sleep(5)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return
        except discord.NotFound:
            return
    else:
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(3)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return
        except discord.NotFound:
            return
        return

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("❌")
        await ctx.send(f"""```⚠ {error}
[ℹ] for more information check the console```""")
        await asyncio.sleep(3)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return
        except discord.NotFound:
            return
        return

@bot.command()
@commands.guild_only()
async def reload(ctx, extension):
    if ctx.message.author.id == 349373972103561218:
        try:
            bot.unload_extension("cogs.{}".format(extension))
        except discord.ext.commands.ExtensionNotLoaded:
            await ctx.send("Cog wasn't loaded, attempting to load", delete_after=5)
        try:
            bot.load_extension("cogs.{}".format(extension))
            await ctx.message.add_reaction("✅")
        except discord.ext.commands.ExtensionAlreadyLoaded:
            await ctx.send("Cog already loaded!", delete_after=5)
        except discord.ext.commands.ExtensionNotFound:
            await ctx.message.add_reaction("❓")
        except discord.ext.commands.NoEntryPointError:
            await ctx.send("Cog doesn't have a setup function!", delete_after=5)
        await asyncio.sleep(5)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return
        except discord.NotFound:
            return
        return
    else:
        await ctx.message.add_reaction('🚫')
        await asyncio.sleep(3)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return
        except discord.NotFound:
            return
        return

@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.message.add_reaction("❌")
        await ctx.send(f"""```⚠ {error}
[ℹ] for more information check the console```""")
        await asyncio.sleep(3)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return
        except discord.NotFound:
            return
        return

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:
            bot.load_extension("cogs.{}".format(filename[:-3]))
        except:
            print("========[ WARNING ]========")
            print(f"An error occurred while loading '{filename}'""")

bot.run(TOKEN, reconnect=True)
