import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
from os import *

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='The one, and only: Botless, created by Pointless#1278.', self_bot=False, pm_help=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Bot online!')
    print('Name: ' + str(bot.user))
    print('ID: ' + str(bot.user.id))

bot.run(os.environ.get('TOKEN'))