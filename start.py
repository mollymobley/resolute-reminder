import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>', description='test')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


with open('token', 'r') as tokenfile:
    token = tokenfile.read().strip()


@bot.command()
async def testcommand():
    pass

bot.run(token)
