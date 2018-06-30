import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import time
import math

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='The one, and only: Botless, created by Pointless#1278.', self_bot=False, pm_help=None)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot online!')
    print('Name: {}'.format(str(bot.user)))
    print('ID: {}'.format(str(bot.user.id)))
    print('Invite Link: https://discordapp.com/oauth2/authorize?client_id=462562571229200384&scope=bot&permissions=2146958591')

@bot.command(pass_context=True)
async def help(ctx, helpc: str = None):
    """This thing"""
    if helpc == None:
        hhelp=discord.Embed(title='Help', color=0x0000FF)
        hhelp.add_field(name='General', value='`help`, `ping`')
        hhelp.set_footer(text='I\'m a bot that has commands that are yet to come!')
        await bot.say(embed=hhelp)
    if helpc:
        helpget = bot.get_command(helpc)
        shelp=discord.Embed(title='Help', color=0x0000FF)
        shelp.add_field(name=f'{helpc}',value=f'Help: {helpget.help}\nUsage: {helpget.signature}')
        return await bot.say(embed=shelp)
    else:
        return
@bot.command(pass_context=True,aliases=['latency','pong'])
async def ping(ctx):
    ptime = time.time()
    embed=discord.Embed(Title = 'Ping', color = 0x00FF00)
    embed.add_field(name = 'Pong!', value = 'Calculating...')
    ping3=await bot.say(embed=embed)
    ping2=time.time() - ptime 
    ping1=discord.Embed(Title = 'Ping', color = 0x00FF00)
    ping1.add_field(name='Pong!', value='{} milliseconds.'.format(int((round(ping2 * 1000)))))
    await bot.edit_message(ping3,embed=ping1)

bot.run(os.environ.get('TOKEN'))