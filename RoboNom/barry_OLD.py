#########################
######## BARRY ##########
########################


### IMPORT LIBRARIES ###

import os
import requests
import json
import typing
import discord
import discord.channel
import cleverbotfreeapi
import random
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand
from discord_slash.model import SlashContext
from googlesearch import search


### SET PREFIX, VARIABLES, and TOKEN ###
bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), case_insensitive=True, intents=discord.Intents.all())
slash = SlashCommand(bot)
#cb = cleverbot.CleverBot()

#Create more secure function so I can push to GitHub without compromising the token
#remember to add this in .gitignore

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


### FUNCTIONS ###

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return(quote)



### EVENTS ###

#startup recognition
@bot.event
async def on_ready():
    print("Bot is online and ready to go!")
    await bot.change_presence(activity=discord.Activity(type=5, name='Collegiate Cyber Defense Competition'))

#voice-channel-update
#currently a non-function, testing voice channel activity notifications
""" @bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 787743717393563698:
            textchannel = bot.get_channel(789521865513107546)
            await textchannel.send('Hey <@645083460658003969>, someone joined the voice channel lol') """
#welcome message, disabled for now
#@bot.event
#async def on_member_join(member):
#    await member.create_dm()
#    await member.dm_channel.send(
#	f'Hi {member.name}, welcome to the server!'
#    )


### COMMANDS ###

#mouthpiece of Sauron
@bot.command()
async def say(ctx, *, input):
    await ctx.message.delete()
    await ctx.send(input)


#measures latency
@bot.command()
async def ping(ctx):
    await ctx.send("It takes a packet " + f'{round (bot.latency * 1000)}ms ' + " to reach your device from the server.")

#nerdy quote
@bot.command()
async def nerdyquote(ctx):
    responses = open('lib/nerdyquotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

#inspirational quote
@bot.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

#chat with barry
@bot.command()
async def robonom(ctx, *, input):
    response = cleverbotfreeapi.cleverbot(input)
    await ctx.send(response)

#8ball
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, input):
    responses = open('lib/8ball.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

#google search
@bot.command()
async def google(ctx, *, query):
    author = ctx.author.mention
    googleresult = await ctx.send(f"Here is the number one result for that query {author}!")
    async with ctx.typing():
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            print("User searched for " + query + " and got " + j)
    await googleresult.edit(content=j)

#Bot info
@bot.command()
async def info(ctx):
    embed = discord.Embed(title='Information about RoboNom', description="Here's some information about me", color=ctx.me.color)

    embed.add_field(name='Creator', value='1NN0M1N473#1337', inline=False)

    embed.add_field(name='Server count', value="I'm in " + f'{len(bot.guilds)}' + " servers!", inline=False)

    embed.add_field(name='Invite', value='[Click here](https://discord.com/oauth2/authorize?client_id=788139657711452190&scope=bot) to invite me to your server', inline=False)

    await ctx.send(embed=embed)
### HELP COMMAND ###

bot.remove_command('help')

@bot.command()
async def help(ctx, argument: typing.Optional[str] = "None"):

    if (argument == "None"):

        embed = discord.Embed(title='RoboNom help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0x00FFFF)

        embed.add_field(name='_ _', value='_ _', inline=False)

        embed.add_field(name='?help commands', value='Shows the commands you can run. Currently the only argument, more to come!', inline=False)

        embed.add_field(name='?help', value='Displays this help screen', inline=False)

        embed.add_field(name='Work in Progress', value='This help screen is consistently being updated with new commands, and will change significantly when I finish integrating cogs.')

        embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')

        embed.add_field(name='_ _', value='_ _', inline=False)

        await ctx.send(embed=embed)


    elif(argument == "commands"):

            embed = discord.Embed(title='RoboNom help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0x00FFFF)

            embed.add_field(name='_ _', value='_ _', inline=False)

            embed.add_field(name='?ping', value='Measures your latency!', inline=False)

            embed.add_field(name='?help', value='Displays usable commands', inline=False)

            embed.add_field(name='?quote', value='Fetches a random quote from the ZenQuote API', inline=False)

            embed.add_field(name='?nerdyquote', value="Fetches a random programming-themed quote", inline=False)

            embed.add_field(name='?robonom <say something>', value="Engage in conversation with the bot; responses not guaranteed to make sense", inline=False)

            embed.add_field(name='?google <search query', value="Returns the number one Google search result for a given query. Can also use dorking parameters like site: and inurl:")

            embed.add_field(name='_ _', value='_ _', inline=False)

            embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')

            await ctx.send(embed=embed)

    else:

        embed = discord.Embed(title='RoboNom help', description='No command found. What exactly are you trying to accomplish? Run ?help again.', color = 0xFF0000)

        embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')

        await ctx.send(embed=embed)


### RUN BOT ###

bot.run(TOKEN)
