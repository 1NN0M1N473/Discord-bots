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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='?help'))

#voice-channel-update
#currently a non-function, testing voice channel activity notifications
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 787743717393563698:
            textchannel = bot.get_channel(789521865513107546)
            await textchannel.send('Test message sent to <@645083460658003969>')
#welcome message, disabled for now
#@bot.event
#async def on_member_join(member):
#    await member.create_dm()
#    await member.dm_channel.send(
#	f'Hi {member.name}, welcome to the server!'
#    )


### COMMANDS ###

#measures latency
@bot.command()
async def ping(ctx):
    await ctx.send("It takes a packet " + f'{round (bot.latency * 1000)}ms ' + " to reach your device from the server.")

#nerdy quote
@bot.command()
async def nerdyquote(ctx):
    responses = open('jokes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

#attack with bees
@bot.command()
async def beeattack(ctx):
    await ctx.send("https://media.giphy.com/media/yIXVnzpoNiE0w/giphy.gif")

#inspirational quote
@bot.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

#chat with barry
@bot.command()
async def barry(ctx, *, input):
    response = cleverbotfreeapi.cleverbot(input)
    await ctx.send(response + "-?-")

@slash.slash(name="test")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])

### HELP COMMAND ###

bot.remove_command('help')

@bot.command()
async def help(ctx, argument: typing.Optional[str] = "None"):

    if (argument == "None"):

        embed = discord.Embed(title='Barry help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0x00FFFF)

        embed.add_field(name='_ _', value='_ _', inline=False)

        embed.add_field(name='?help commands', value='Shows the commands you can run. Currently the only argument, more to come!', inline=False)

        embed.add_field(name='?help', value='Displays this help screen', inline=False)

        embed.set_footer(text='This bot was created by 1NN0M1N473#1337', icon_url='https://i.imgur.com/SRvpDj5.jpg')

        embed.add_field(name='_ _', value='_ _', inline=False)

        await ctx.send(embed=embed)


    elif(argument == "commands"):

            embed = discord.Embed(title='Barry help', description=("Hi there {}! Here are the commands you can use with this bot:".format(ctx.message.author.mention)), color = 0x00FFFF)

            embed.add_field(name='_ _', value='_ _', inline=False)

            embed.add_field(name='?ping', value='Measures your latency!', inline=False)

            embed.add_field(name='?help', value='Displays usable commands', inline=False)

            embed.add_field(name='?quote', value='Fetches a random quote from the ZenQuote API', inline=False)

            embed.add_field(name='?nerdyquote', value="Fetches a random programming-themed quote", inline=False)

            embed.add_field(name='?beeattack', value="Summons a horde of angry bees, use with caution", inline=False)

            embed.add_field(name='?barry <say something>', value="Engage in conversation with the bot; responses not guaranteed to make sense", inline=False)

            embed.add_field(name='_ _', value='_ _', inline=False)

            await ctx.send(embed=embed)

    else:

        embed = discord.Embed(title='Barry help', description='No command found. What exactly are you trying to accomplish? Run ?help again.', color = 0xFF0000)
        await ctx.send(embed=embed)


### RUN BOT ###

bot.run(TOKEN)
