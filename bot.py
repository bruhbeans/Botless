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
    await print('Bot online!')
    await print('Name: {}'.format(str(bot.user)))
    await print('ID: {}'.format(str(bot.user.id)))
    await print('Invite Link: https://discordapp.com/oauth2/authorize?client_id=462562571229200384&scope=bot&permissions=2146958591')

@bot.event
async def on_member_join(member):
    channel = await bot.get_channel(431850419392741398)
    await bot.send_message(channel, f'Welcome, {member}, to Botless\' support server!')

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