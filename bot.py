import discord
from discord.ext import commands
import os
import time
import random
import math
import statistics
import requests
import psutil

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='The one, and only: Botless, created by Pointless#1278.', self_bot=False)
bot.remove_command('help')


def pointcheck(ctx):
    return ctx.message.author.id == '276043503514025984'  # checks if @Pointless#1278 is the author of the command


@bot.event
async def on_ready():
    print('Bot online!')
    print('Name: {}'.format(str(bot.user)))
    print('ID: {}'.format(str(bot.user.id)))
    print('Invite Link: https://discordapp.com/oauth2/authorize?client_id=462562571229200384&scope=bot&permissions=2146958591')
    await bot.change_presence(game=discord.Game(name=f'over {len(bot.servers)} servers | !help',type=3))


'''
'##::::'##:'########:'##:::::::'########::                                                                                      
 ##:::: ##: ##.....:: ##::::::: ##.... ##:                                                                                      
 ##:::: ##: ##::::::: ##::::::: ##:::: ##:                                                                                      
 #########: ######::: ##::::::: ########::                                                                                      
 ##.... ##: ##...:::: ##::::::: ##.....:::                                                                                      
 ##:::: ##: ##::::::: ##::::::: ##::::::::                                                                                      
 ##:::: ##: ########: ########: ##::::::::                                                                                      
..:::::..::........::........::..:::::::::     '''


@bot.command(pass_context=True, aliases=['commands', 'cmds'])
async def help(ctx,helpc: str=None):
    '''Get the list of commands.\nUsage: !help [command]\nAliases: !commands, !cmds\nPermissions: None'''
    if helpc == None:
        hhelp = discord.Embed(title='Help', color=0x0000FF)
        hhelp.add_field(name='General', value='`help` `ping` `info` `suggest`')
        hhelp.add_field(name='Informational', value='`cryptocurrency` `math`')
        hhelp.add_field(name='Fun', value='`coinflip` `8ball` `comic` `dog`')
        hhelp.add_field(name='Utility', value='`part` `roll` `serverinfo`')
        hhelp.add_field(name='Managing', value='`giverole` `takerole`')
        hhelp.add_field(name='Moderation', value='`kick` `ban` `unban` `softban` `channelmute` `channelunmute` `warn` `purge`')
        hhelp.add_field(name='Owner', value='`say` `restart`')
        hhelp.set_footer(text='Do !help <command> to find out what it does.')
        await bot.say(embed=hhelp)
    if helpc:
        helpget = bot.get_command(helpc)
        shelp = discord.Embed(title='Help', color=0x0000FF)
        shelp.add_field(name=f'Command: !{helpc}', value=f'Help: {helpget.help}')
        return await bot.say(embed=shelp)
    else:
        return


'''
:'#######::'##:::::'##:'##::: ##:'########:'########::                                                                          
'##.... ##: ##:'##: ##: ###:: ##: ##.....:: ##.... ##:                                                                          
 ##:::: ##: ##: ##: ##: ####: ##: ##::::::: ##:::: ##:                                                                          
 ##:::: ##: ##: ##: ##: ## ## ##: ######::: ########::                                                                          
 ##:::: ##: ##: ##: ##: ##. ####: ##...:::: ##.. ##:::                                                                          
 ##:::: ##: ##: ##: ##: ##:. ###: ##::::::: ##::. ##::                                                                          
. #######::. ###. ###:: ##::. ##: ########: ##:::. ##:                                                                          
:.......::::...::...:::..::::..::........::..:::::..::  '''


@bot.command(pass_context=True)
@commands.check(pointcheck)
async def say(ctx, *, text: str=None):
    '''Make the bot say something of your choice.\nUsage: !say <text>\nAliases: None\nPermissions: Bot Owner'''
    await bot.delete_message(ctx.message)
    await bot.say(text)


@bot.command(pass_context=True, aliases=['shutdown'])
@commands.check(pointcheck)
async def restart(ctx):
    '''Stop and run the bot again.\nUsage: !restart\nAliases: !shutdown\nPermissions: Bot Owner'''
    embed = discord.Embed(title='Restart', description=f'Sorry, but {ctx.message.author.mention} has forced me to restart. It\'ll only take a moment!', color=0xFF0000)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)
    await bot.logout()


'''
:'######:::'########:'##::: ##:'########:'########:::::'###::::'##:::::::                                                       
'##... ##:: ##.....:: ###:: ##: ##.....:: ##.... ##:::'## ##::: ##:::::::                                                       
 ##:::..::: ##::::::: ####: ##: ##::::::: ##:::: ##::'##:. ##:: ##:::::::                                                       
 ##::'####: ######::: ## ## ##: ######::: ########::'##:::. ##: ##:::::::                                                       
 ##::: ##:: ##...:::: ##. ####: ##...:::: ##.. ##::: #########: ##:::::::                                                       
 ##::: ##:: ##::::::: ##:. ###: ##::::::: ##::. ##:: ##.... ##: ##:::::::                                                       
. ######::: ########: ##::. ##: ########: ##:::. ##: ##:::: ##: ########:                                                       
:......::::........::..::::..::........::..:::::..::..:::::..::........::        '''


@bot.command(pass_context=True, aliases=['latency', 'pong'])
async def ping(ctx):
    '''Find the response time in milliseconds.\nUsage: !ping\nAliases: !latency, !pong\nPermissions: None'''
    ptime = time.time()
    embed = discord.Embed(Title='Ping', color=0x00FF00)
    embed.add_field(name='Pong!', value='Calculating...')
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    ping3 = await bot.say(embed=embed)
    ping2 = time.time() - ptime 
    ping1 = discord.Embed(Title='Ping', color=0x00FF00)
    ping1.add_field(name='Pong!', value='{} milliseconds.'.format(int((round(ping2 * 1000)))))
    ping1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.edit_message(ping3, embed=ping1)


@bot.command(pass_context=True, aliases=['stats', 'statistics', 'information'])
async def info(ctx):
    '''All the info\'s here!\nUsage: !info\nAliases: !stats, !statistics, !information\nPermissions: None'''
    memory = psutil.virtual_memory()
    usedmemory = memory.used >> 30
    percentmemoryused = memory.percent
    freememory = memory.free >> 30
    sinfo = discord.Embed(title='Information', color=0x00FF00)
    sinfo.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    sinfo.add_field(name='Servers', value='{} servers.'.format(str(len(bot.servers))))
    sinfo.add_field(name='Discord.py version', value='Version {}'.format(discord.__version__))
    sinfo.add_field(name='Memory Usage', value='{} gigabytes ({}%) used, with {} gigabytes left over.'.format(usedmemory, int(percentmemoryused), freememory))
    sinfo.add_field(name='Links', value='[Support Server](https://discord.gg/JpnSpyg \"Support Server\")\n[Invite Link](https://discordapp.com/oauth2/authorize?client_id=462562571229200384&scope=bot&permissions=2146958591 \"Invite Link\")')
    sinfo.set_thumbnail(url = bot.user.avatar_url)
    await bot.say(embed=sinfo)

@bot.command(pass_context=True)
async def suggest(ctx, *, idea):
    '''Suggest anything!\nUsage: !suggest <suggestion>\nAliases: None\nPermissions: None'''
    if idea == None:
        nsuggest = discord.Embed(title='Error',description='Specify a suggestion!',color=0xFF0000)
        nsuggest.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=nsuggest)
    if idea:
        osuggest = discord.Embed(title='Suggest',description=idea,color=0x00FF00)
        osuggest.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.send_message(discord.Object(id='431958602148872222'), embed=osuggest)
        ssuggest = discord.Embed(title='Suggest',description='Sent that suggestion over! Thank you!',color=0x00FF00)
        ssuggest.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=ssuggest)
        themessage = await bot.say(embed=osuggest)
        await bot.add_reaction(themessage, '\U0001F44E')
        await bot.add_reaction(themessage, '\U0001F44D')
    else:
        pass

'''
'####:'##::: ##:'########::'#######::'########::'##::::'##::::'###::::'########:'####::'#######::'##::: ##::::'###::::'##:::::::
. ##:: ###:: ##: ##.....::'##.... ##: ##.... ##: ###::'###:::'## ##:::... ##..::. ##::'##.... ##: ###:: ##:::'## ##::: ##:::::::
: ##:: ####: ##: ##::::::: ##:::: ##: ##:::: ##: ####'####::'##:. ##::::: ##::::: ##:: ##:::: ##: ####: ##::'##:. ##:: ##:::::::
: ##:: ## ## ##: ######::: ##:::: ##: ########:: ## ### ##:'##:::. ##:::: ##::::: ##:: ##:::: ##: ## ## ##:'##:::. ##: ##:::::::
: ##:: ##. ####: ##...:::: ##:::: ##: ##.. ##::: ##. #: ##: #########:::: ##::::: ##:: ##:::: ##: ##. ####: #########: ##:::::::
: ##:: ##:. ###: ##::::::: ##:::: ##: ##::. ##:: ##:.:: ##: ##.... ##:::: ##::::: ##:: ##:::: ##: ##:. ###: ##.... ##: ##:::::::
'####: ##::. ##: ##:::::::. #######:: ##:::. ##: ##:::: ##: ##:::: ##:::: ##::::'####:. #######:: ##::. ##: ##:::: ##: ########:
....::..::::..::..:::::::::.......:::..:::::..::..:::::..::..:::::..:::::..:::::....:::.......:::..::::..::..:::::..::........::'''


@bot.command(pass_context=True, aliases=['cc'])
async def cryptocurrency(ctx, coin:str=None):
    '''Find out cryptocurrency rates.\nUsage: !cryptocurrency <cryptocurrency symbol>\nAliases: !cc\nPermissions: None'''
    r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + str(coin) + '&tsyms=USD')
    json = r.json()
    if r.status_code == 200:
        if coin == None:
            ncryptocurrency = discord.Embed(title='Error', description='Specify the cryptocurrency symbol!', color=0xFF0000)
            ncryptocurrency.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=ncryptocurrency)
        if coin:
            scryptocurrency = discord.Embed(title='Cryptocurrency', description='Information about the cryptocurrency, {}.'.format(str(coin)), color=0x00FF00)
            scryptocurrency.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            scryptocurrency.add_field(name='Price', value=json['DISPLAY'][str(coin)]['USD']['PRICE'])
            scryptocurrency.add_field(name='Highest Price Today', value=json['DISPLAY'][str(coin)]['USD']['HIGHDAY'])
            scryptocurrency.add_field(name='Lowest Price Today', value=json['DISPLAY'][str(coin)]['USD']['LOWDAY'])
            scryptocurrency.add_field(name='Last Updated', value=json['DISPLAY'][str(coin)]['USD']['LASTUPDATE'])
            scryptocurrency.add_field(name='Supply', value=json['DISPLAY'][str(coin)]['USD']['SUPPLY'])
            scryptocurrency.set_footer(text='Cryptocurrency rates by https://cryptocompare.com/!')
            return await bot.say(embed=scryptocurrency)
        else:
            return
    else:
        rcryptocurrency = discord.Embed(title='Error', description='I could not access the API! Direct Message Pointless#1278 so this can be fixed! (You will be credited for finding it out!)', color=0xFF0000)
        rcryptocurrency.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rcryptocurrency)


'''
'########:'##::::'##:'##::: ##:
 ##.....:: ##:::: ##: ###:: ##:
 ##::::::: ##:::: ##: ####: ##:
 ######::: ##:::: ##: ## ## ##:
 ##...:::: ##:::: ##: ##. ####:
 ##::::::: ##:::: ##: ##:. ###:
 ##:::::::. #######:: ##::. ##:
..:::::::::.......:::..::::..::
'''


@bot.command(pass_context=True)
async def coinflip(ctx):
    '''Flip a coin and either get heads or tails.\nUsage: !coinflip \nAliases: None\nPermissions: None'''
    scoinflip = discord.Embed(title='Coinflip', description=random.choice(['Heads', 'Tails']), color=0xFF0000)
    scoinflip.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=scoinflip)


@bot.command(pass_context=True, name='8ball', aliases=['8b', 'eb'])
async def eightball(ctx, question:str=None):
    '''Ask a question and let the magic eightball answer for you!\nUsage: !eightball <question> \nAliases: None\nPermissions: None'''
    if question == None:
        neightball = discord.Embed(title='Error', description='Specify the question!', color=0xFF0000)
        neightball.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=neightball)
    if '?' not in question:
        qeightball = discord.Embed(title='Error', description='That is invalid and not a question!', color=0xFF0000)
        qeightball.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=qeightball)
    else:
        seightball = discord.Embed(title='8ball', description=random.choice(['Signs point to yes.', 'Yes.', 'Without a doubt.', 'As I see it, yes.', 'You may rely on it.', 'It is decidedly so.', 'Yes - definitely.', 'It is certain.', 'Most likely.', 'Outlook good.', 'Reply hazy, try again.', 'Concentrate and ask again.', 'Better not tell you now.', 'Cannot predict now.', 'Ask again later.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'My reply is no.', 'Don\'t count on it.']), color=0x00FF00)
        seightball.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=seightball)

    
@bot.command(pass_context=True, aliases=['xkcd'])
async def comic(ctx):
    '''Check out a random comic, with a total of 2013 comics!.\nUsage: !comic\nAliases: !xkcd\nPermissions: None'''
    r = requests.get(f'https://xkcd.com/{random.randint(1,2013)}/info.0.json')
    json = r.json()
    if r.status_code == 200:
        scomic = discord.Embed(title='Comic', description=str(json['title']), color=0x00FF00)
        scomic.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        scomic.set_image(url=json['img'])
        scomic.set_footer(text='Comics by https://xkcd.com/!')
        return await bot.say(embed=scomic)
    else:
        rcomic = discord.Embed(title='Error', description='I could not access the API! Direct Message Pointless#1278 so this can be fixed! (You will be credited for finding it out!)', color=0xFF0000)
        rcomic.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rcomic)


@bot.command(pass_context=True)
async def dog(ctx):
    '''Check out a random cute or funny cat!\nUsage: !cat\nAliases: None\nPermissions: None'''
    r = requests.get(f'https://api.thedogapi.co.uk/v2/dog.php/')
    json = r.json()
    if r.status_code == 200:
        sdog = discord.Embed(title='Dog', description='A random cute dog!', color=0x00FF00)
        sdog.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        sdog.set_image(url=json['data'][0]['url'])
        sdog.set_footer(text='Dogs by http://thedogapi.co.uk/!')
        return await bot.say(embed=sdog)
    else:
        rdog = discord.Embed(title='Error', description='I could not access the API! Direct Message Pointless#1278 so this can be fixed! (You will be credited for finding it out!)', color=0xFF0000)
        rdog.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rdog)


'''
'##::::'##:'########:'####:'##:::::::'####:'########:'##:::'##:
 ##:::: ##:... ##..::. ##:: ##:::::::. ##::... ##..::. ##:'##::
 ##:::: ##:::: ##::::: ##:: ##:::::::: ##::::: ##:::::. ####:::
 ##:::: ##:::: ##::::: ##:: ##:::::::: ##::::: ##::::::. ##::::
 ##:::: ##:::: ##::::: ##:: ##:::::::: ##::::: ##::::::: ##::::
 ##:::: ##:::: ##::::: ##:: ##:::::::: ##::::: ##::::::: ##::::
. #######::::: ##::::'####: ########:'####:::: ##::::::: ##::::
:.......::::::..:::::....::........::....:::::..::::::::..:::::
'''


@bot.command(pass_context=True)
async def part(ctx, *choice):
    '''Make Botless take a letter out of any word!\nUsage: !part <word>\nAliases: None\nPermissions: None'''
    spart = discord.Embed(title='Part', description=str(random.choice(*choice)), color=0x00FF00)
    spart.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=spart)

@bot.command(pass_context=True)
async def roll(ctx, maxnumber:int=6):
    '''A roll command!\nUsage: !roll <maxnumber>\nAliases: None\nPermissions: None'''
    if maxnumber == None:
        nroll = discord.Embed(title='Error', description=f'Specify a maximum number!', color=0xFF0000)
        nroll.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nroll)
    sroll = discord.Embed(title='Roll', description=f'You rolled a {random.randint(1,maxnumber)}!', color=0x00FF00)
    sroll.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sroll)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    '''See information about the server!\nUsage: !serverinfo\nAliases: None\nPermissions: None'''

    sserverinfo = discord.Embed(title = (str(ctx.message.server.name)), colour = 0x00FF00)
    sserverinfo.set_thumbnail(url = ctx.message.server.icon_url)
    sserverinfo.add_field(name = 'Owner', value = str(ctx.message.server.owner))
    sserverinfo.add_field(name = 'ID', value = str(ctx.message.server.id))
    sserverinfo.add_field(name = 'Member Count', value = str(ctx.message.server.member_count))
    sserverinfo.add_field(name = 'Region', value = str(ctx.message.server.region))
    sserverinfo.add_field(name = 'AFK Timeout', value = str(ctx.message.server.afk_timeout))
    sserverinfo.add_field(name = 'AFK Channel', value = str(ctx.message.server.afk_channel))
    sserverinfo.add_field(name = 'Verification Level', value = str(ctx.message.server.verification_level))
    sserverinfo.add_field(name = 'Custom Emotes', value=len(ctx.message.server.emojis))
    sserverinfo.add_field(name = 'Channels', value=len(ctx.message.server.channels))
    sserverinfo.add_field(name = 'Features', value=str(ctx.message.server.features))
    sserverinfo.set_footer(text =f'Created at: {str(ctx.message.server.created_at)}')
    await bot.say(embed=sserverinfo)
'''
'##::::'##::::'###::::'########:'##::::'##:
 ###::'###:::'## ##:::... ##..:: ##:::: ##:
 ####'####::'##:. ##::::: ##:::: ##:::: ##:
 ## ### ##:'##:::. ##:::: ##:::: #########:
 ##. #: ##: #########:::: ##:::: ##.... ##:
 ##:.:: ##: ##.... ##:::: ##:::: ##:::: ##:
 ##:::: ##: ##:::: ##:::: ##:::: ##:::: ##:
..:::::..::..:::::..:::::..:::::..:::::..::
'''


@bot.group(pass_context=True, aliases=['maths', 'mathematics'])
async def math(ctx):
    '''Get a list of mathematical commands.\nUsage: !math [child command]\nAliases: !maths, !mathematics\nPermissions: None'''
    if ctx.invoked_subcommand == None:
        smath = discord.Embed(title='Math', description='My child commands: `add` `subtract` `multiply` `d̶i̶v̶i̶d̶e̶` `factorial` `gcd` `median` `medianlow` `medianhigh`', color=0x0000FF)
        smath.set_footer(text='Do `!math <child command>` to execute one.')
        smath.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=smath)
    else:
        pass


@math.command(pass_context=True)
async def add(ctx, a, b):
    '''Add two numbers.\nUsage: !add <number1> <number2>\nAliases: None\nPermissions: None'''
    if a == None:
        nadd1 = discord.Embed(title='Error', description='Specify the first number!', color=0xFF0000)
        nadd1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nadd1)
    if b == None:
        nadd2 = discord.Embed(title='Error', description='Specify the second number!', color=0xFF0000)
        nadd2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nadd2)
    sadd = discord.Embed(title='Add', description=int(a) + int(b), color=0x00FF00)
    sadd.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sadd)


@math.command(pass_context=True)
async def subtract(ctx, a, b):
    '''Subtract two numbers.\nUsage: !subtract <number1> <number2>\nAliases: None\nPermissions: None'''
    if a == None:
        nsubtract1 = discord.Embed(title='Error', description='Specify the first number!', color=0xFF0000)
        nsubtract1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nsubtract1)
    if b == None:
        nsubtract2 = discord.Embed(title='Error', description='Specify the second number!', color=0xFF0000)
        nsubtract2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nsubtract2)
    ssubtract = discord.Embed(title='Subtract', description=int(a) - int(b), color=0x00FF00)
    ssubtract.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=ssubtract)


@math.command(pass_context=True)
async def multiply(ctx, a, b):
    '''Multiply two numbers.\nUsage: !multiply <number1> <number2>\nAliases: None\nPermissions: None'''
    if a == None:
        nmultiply1 = discord.Embed(title='Error', description='Specify the first number!', color=0xFF0000)
        nmultiply1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nmultiply1)
    if b == None:
        nmultiply2 = discord.Embed(title='Error', description='Specify the second number!', color=0xFF0000)
        nmultiply2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nmultiply2)
    smultiply = discord.Embed(title='Multiply', description=int(a) * int(b), color=0x00FF00)
    smultiply.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=smultiply)


@math.command(pass_context=True)
async def divide(ctx, a, b):
    '''Divide two numbers.\nUsage: !divide <number1> <number2>\nAliases: None\nPermissions: None'''
    if a == None:
        ndivide1 = discord.Embed(title='Error', description='Specify the first number!', color=0xFF0000)
        ndivide1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ndivide1)
    if b == None:
        ndivide2 = discord.Embed(title='Error', description='Specify the second number!', color=0xFF0000)
        ndivide2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ndivide2)
    sdivide = discord.Embed(title='Divide', description=int(a) / int(b), color=0x00FF00)
    sdivide.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sdivide)


@math.command(pass_context=True)
async def factorial(ctx, a):
    '''Find the factorial of a number.\nUsage: !factorial <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nfactorial = discord.Embed(title='Error', description='Specify the number!', color=0xFF0000)
        nfactorial.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nfactorial)
    sfactorial = discord.Embed(title='Factorial', description=math.factorial(int(a)), color=0x00FF00)
    sfactorial.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sfactorial)


"""
@math.command(pass_context=True)
async def floor(ctx,a):
    '''Find the floor of a number.\nUsage: !floor <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nfloor=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nfloor.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nfloor)
    sfloor=discord.Embed(title='Floor',description=math.floor(int(a)),color=0x00FF00)
    sfloor.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sfloor)
"""


@math.command(pass_context=True, aliases=['hcf'])
async def gcd(ctx, a, b):
    '''Find the greatest common divisor (highest common factor) of two numbers.\nUsage: !gcd <number1> <number2>\nAliases: !hcf\nPermissions: None'''
    if a == None:
        ngcd1 = discord.Embed(title='Error', description='Specify the first number!', color=0xFF0000)
        ngcd1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ngcd1)
    if b == None:
        ngcd2 = discord.Embed(title='Error', description='Specify the second number!', color=0xFF0000)
        ngcd2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ngcd2)
    sgcd = discord.Embed(title='Greatest Common Divisor (Highest Common Factor)', description=math.gcd(int(a), int(b)), color=0x00FF00)
    sgcd.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sgcd)


"""
@math.command(pass_context=True)
async def exp(ctx,a):
    '''Find the e constant to the power of a number.\nUsage: !exp <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nexp=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nexp.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nexp)
    sexp=discord.Embed(title='Floor',description=math.exp(int(a)),color=0x00FF00)
    sexp.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sexp)

@math.command(pass_context=True)
async def expone(ctx,a):
    '''Find the e constant to the power of a number minus 1.\nUsage: !exp <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nexpone=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nexpone.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nexpone)
    sexpone=discord.Embed(title='Floor',description=math.expm1(int(a)),color=0x00FF00)
    sexpone.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sexpone)

@math.command(pass_context=True)
async def logarithm(ctx,a):
    '''Find the natural logarithm of a number to the base of the e constant.\nUsage: !logarithm <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nlogarithm=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nlogarithm.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nlogarithm)
    slogarithm=discord.Embed(title='Natural Logarithm',description=math.log(int(a)),color=0x00FF00)
    slogarithm.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=slogarithm)

@math.command(pass_context=True)
async def logarithmbase(ctx,a,b):
    '''Find the logarithm of a number to a base.\nUsage: !logarithmbase <number> <base>\nAliases: None\nPermissions: None'''
    if a == None:
        nlogarithmbase1=discord.Embed(title='Error',description='Specify the first number!',color=0xFF0000)
        nlogarithmbase1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nlogarithmbase1)
    if b == None:
        nlogarithmbase2=discord.Embed(title='Error',description='Specify the base!',color=0xFF0000)
        nlogarithmbase2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nlogarithmbase2)
    slogarithmbase=discord.Embed(title='Logarithm',description=math.log(int(a),int(b)),color=0x00FF00)
    slogarithmbase.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=slogarithm)

@math.command(pass_context=True)
async def logarithmonep(ctx,a):
    '''Find the natural logarithm of 1 + a number (base e).\nUsage: !logarithmonep <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nlogarithmonep=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nlogarithmonep.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nlogarithmonep)
    slogarithmonep=discord.Embed(title='Natural Logarithm + 1',description=math.log1p(int(a)),color=0x00FF00)
    slogarithmonep.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=slogarithmonep)

@math.command(pass_context=True)
async def logarithmtwo(ctx,a):
    '''Find the base-2 logarithm of a number.\nUsage: !logarithmtwo <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nlogarithmtwo=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nlogarithmtwo.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nlogarithmtwo)
    slogarithmtwo=discord.Embed(title='Base-2 Logarithm',description=math.log2(int(a)),color=0x00FF00)
    slogarithmtwo.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=slogarithmtwo)

@math.command(pass_context=True)
async def logarithmten(ctx,a):
    '''Find the base-10 logarithm of a number.\nUsage: !logarithmten <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nlogarithmten=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nlogarithmten.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nlogarithmtwo)
    slogarithmten=discord.Embed(title='Base-10 Logarithm',description=math.log10(int(a)),color=0x00FF00)
    slogarithmten.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=slogarithmten)

@math.command(pass_context=True)
async def exponent(ctx,a,b):
    '''Find the exponent of a number.\nUsage: !exponent <number> <power to>\nAliases: None\nPermissions: None'''
    if a == None:
        nexponent1=discord.Embed(title='Error',description='Specify the first number!',color=0xFF0000)
        nexponent1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nexponent1)
    if b == None:
        nexponent2=discord.Embed(title='Error',description='Specify the second number!',color=0xFF0000)
        nexponent2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nexponent2)
    sexponent=discord.Embed(title='Exponent',description=math.pow(int(a),int(b)),color=0x00FF00)
    sexponent.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sexponent)

@math.command(pass_context=True)
async def sqrt(ctx,a):
    '''Find the square root of a number.\nUsage: !sqrt <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nsqrt=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nsqrt.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nsqrt)
    ssqrt=discord.Embed(title='Square Root',description=math.sqrt(int(a)),color=0x00FF00)
    ssqrt.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=ssqrt)

@math.command(pass_context=True)
async def acos(ctx,a):
    '''Find the arc cosine of a number, in radians.\nUsage: !acos <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nacos=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nacos.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nacos)
    sacos=discord.Embed(title='Arc Cosine',description=math.acos(int(a)),color=0x00FF00)
    sacos.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sacos)

@math.command(pass_context=True)
async def asin(ctx,a):
    '''Find the arc sine of a number, in radians.\nUsage: !asin <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nasin=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nasin.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nasin)
    sasin=discord.Embed(title='Arc Sine',description=math.asin(int(a)),color=0x00FF00)
    sasin.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sasin)

@math.command(pass_context=True)
async def atan(ctx,a):
    '''Find the arc tangent of a number, in radians.\nUsage: !atan <number>\nAliases: None\nPermissions: None'''
    if a == None:
        natan=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        natan.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=natan)
    satan=discord.Embed(title='Arc Tangent',description=math.asin(int(a)),color=0x00FF00)
    satan.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=satan)

@math.command(pass_context=True)
async def atantwo(ctx,a,b):
    '''Find atan(number1 / number2).\nUsage: !atantwo <number1> <number2>\nAliases: None\nPermissions: None'''
    if a == None:
        natantwo1=discord.Embed(title='Error',description='Specify the first number!',color=0xFF0000)
        natantwo1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=natantwo1)
    if b == None:
        natantwo2=discord.Embed(title='Error',description='Specify the second number!',color=0xFF0000)
        natantwo2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=natantwo2)
    satantwo=discord.Embed(title='Arc Tangent x (Number 1 ÷ Number 2)',description=math.atan2(int(a),int(b)),color=0x00FF00)
    satantwo.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=satantwo)

@math.command(pass_context=True)
async def cos(ctx,a):
    '''Find the cosine of a number, in radians.\nUsage: !cos <number>\nAliases: None\nPermissions: None'''
    if a == None:
        ncos=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        ncos.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ncos)
    scos=discord.Embed(title='Cosine',description=math.cos(int(a)),color=0x00FF00)
    scos.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=scos)

@math.command(pass_context=True)
async def euclidean(ctx,a,b):
    '''Find the Euclidean norm of two numbers.\nUsage: !euclidean <number1> <number2>\nAliases: None\nPermissions: None'''
    if a == None:
        neuclidean1=discord.Embed(title='Error',description='Specify the first number!',color=0xFF0000)
        neuclidean1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=neuclidean1)
    if b == None:
        neuclidean2=discord.Embed(title='Error',description='Specify the second number!',color=0xFF0000)
        neuclidean2.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=neuclidean2)
    seuclidean=discord.Embed(title='Euclidean Norm',description=math.hypot(int(a),int(b)),color=0x00FF00)
    seuclidean.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=seuclidean)

@math.command(pass_context=True)
async def acosh(ctx,a):
    '''Find the inverse hyperbolic cosine of a number\nUsage: !acosh <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nacosh=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nacosh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nacosh)
    sacosh=discord.Embed(title='Inverse Hyperbolic Cosine',description=math.acosh(int(a)),color=0x00FF00)
    sacosh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sacosh)

@math.command(pass_context=True)
async def cosh(ctx,a):
    '''Find the hyperbolic cosine of a number\nUsage: !cosh <number>\nAliases: None\nPermissions: None'''
    if a == None:
        ncosh=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        ncosh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ncosh)
    sacosh=discord.Embed(title='Hyperbolic Cosine',description=math.acosh(int(a)),color=0x00FF00)
    sacosh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sacosh)

@math.command(pass_context=True)
async def asinh(ctx,a):
    '''Find the inverse hyperbolic sine of a number\nUsage: !asinh <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nasinh=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nasinh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nasinh)
    sasinh=discord.Embed(title='Inverse Hyperbolic Sine',description=math.asinh(int(a)),color=0x00FF00)
    sasinh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sasinh)

@math.command(pass_context=True)
async def sinh(ctx,a):
    '''Find the hyperbolic sine of a number\nUsage: !sinh <number>\nAliases: None\nPermissions: None'''
    if a == None:
        nsinh=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        nsinh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nsinh)
    ssinh=discord.Embed(title='Hyperbolic Sine',description=math.sinh(int(a)),color=0x00FF00)
    ssinh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=ssinh)

@math.command(pass_context=True)
async def atanh(ctx,a):
    '''Find the inverse hyperbolic tangent of a number\nUsage: !atanh <number>\nAliases: None\nPermissions: None'''
    if a == None:
        natanh=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        natanh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=natanh)
    satanh=discord.Embed(title='Inverse Hyperbolic Tanget',description=math.atanh(int(a)),color=0x00FF00)
    satanh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=satanh)

@math.command(pass_context=True)
async def tanh(ctx,a):
    '''Find the hyperbolic tangent of a number\nUsage: !tanh <number>\nAliases: None\nPermissions: None'''
    if a == None:
        ntanh=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        ntanh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ntanh)
    stanh=discord.Embed(title='Hyperbolic Tanget',description=math.tanh(int(a)),color=0x00FF00)
    stanh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=stanh)

@math.command(pass_context=True)
async def gamma(ctx,a):
    '''Find the gamma (Γ) of a number\nUsage: !gamma <number>\nAliases: None\nPermissions: None'''
    if a == None:
        ngamma=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        ngamma.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ngamma)
    sgamma=discord.Embed(title='Gamma Function',description=math.gamma(int(a)),color=0x00FF00)
    sgamma.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sgamma)

@math.command(pass_context=True)
async def lgamma(ctx,a):
    '''Find the natural logarithm of the absolute value of gamma (Γ) at a number\nUsage: !lgamma <number>\nAliases: None\nPermissions: None'''
    if a == None:
        ngammal=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        ngammal.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ngammal)
    sgammal=discord.Embed(title='Natural Logarithm of Absolute Value of Gamma Function at a Number',description=math.lgamma(int(a)),color=0x00FF00)
    sgammal.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sgammal)

@math.command(pass_context=True)
async def pi(ctx,a):
    '''Find the pi (π) × by a number.\nUsage: !pi <number>\nAliases: None\nPermissions: None'''
    if a == None:
        npi=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        npi.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=npi)
    spi=discord.Embed(title='Pi (π)',description=math.pi * int(a),color=0x00FF00)
    spi.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=spi)

@math.command(pass_context=True)
async def e(ctx,a):
    '''Find the e (e) × by a number.\nUsage: !e <number>\nAliases: None\nPermissions: None'''
    if a == None:
        ne=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        ne.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ne)
    se=discord.Embed(title='e (e)',description=math.e * int(a),color=0x00FF00)
    se.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=se)

@math.command(pass_context=True)
async def tau(ctx,a):
    '''Find the tau (τ or 2π) × by a number.\nUsage: !tau <number>\nAliases: None\nPermissions: None'''
    if a == None:
        ntau=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        ntau.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ntau)
    stau=discord.Embed(title='Tau (τ)',description=math.tau * int(a),color=0x00FF00)
    stau.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=stau)

@math.command(pass_context=True)
async def polar(ctx,a):
    '''Find the representation of a number in polar co-ordinates.\nUsage: !polar <number>\nAliases: None\nPermissions: None'''
    if a == None:
        npolar=discord.Embed(title='Error',description='Specify the number!',color=0xFF0000)
        npolar.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=npolar)
    spolar=discord.Embed(title='Polar',description=cmath.polar(int(a)),color=0x00FF00)
    spolar.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=spolar)

@math.command(pass_context=True)
async def mean(ctx,a):
    '''Find the mean of a list of numbers.\nUsage: !mean <[number1, number2, number3, ...]>\nAliases: None\nPermissions: None'''
    if a == None:
        nmean=discord.Embed(title='Error',description='Specify the numbers!',color=0xFF0000)
        nmean.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nmean)
    smean=discord.Embed(title='Mean',description=statistics.mean(list(a)),color=0x00FF00)
    smean.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=smean)

@math.command(pass_context=True)
async def harmonicmean(ctx,a):
    '''Find the harmonic mean of a list of numbers.\nUsage: !harmonicmean <[number1, number2, number3, ...]>\nAliases: None\nPermissions: None'''
    if a == None:
        nharmonicmean=discord.Embed(title='Error',description='Specify the numbers!',color=0xFF0000)
        nharmonicmean.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nharmonicmean)
    sharmonicmean=discord.Embed(title='Mean',description=statistics.harmonic_mean(list(a)),color=0x00FF00)
    sharmonicmean.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=sharmonicmean)
"""


@math.command(pass_context=True)
async def median(ctx, a):
    '''Find the median (middle value) of a list of numbers.\nUsage: !median <[number1, number2, number3, ...]>\nAliases: None\nPermissions: None'''
    if a == None:
        nmedian = discord.Embed(title='Error', description='Specify the numbers!', color=0xFF0000)
        nmedian.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nmedian)
    smedian = discord.Embed(title='Median', description=statistics.median(list(a)), color=0x00FF00)
    smedian.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=smedian)


@math.command(pass_context=True)
async def medianlow(ctx, a):
    '''Find the low median (lowest of a middle value) of a list of numbers.\nUsage: !medianlow <[number1, number2, number3, ...]>\nAliases: None\nPermissions: None'''
    if a == None:
        nmedianlow = discord.Embed(title='Error', description='Specify the numbers!', color=0xFF0000)
        nmedianlow.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nmedianlow)
    smedianlow = discord.Embed(title='Low Median', description=statistics.median_low(list(a)), color=0x00FF00)
    smedianlow.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=smedianlow)


@math.command(pass_context=True)
async def medianhigh(ctx, a):
    '''Find the high median (highest of a middle value) of a list of numbers.\nUsage: !medianhigh <[number1, number2, number3, ...]>\nAliases: None\nPermissions: None'''
    if a == None:
        nmedianhigh = discord.Embed(title='Error', description='Specify the numbers!', color=0xFF0000)
        nmedianhigh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nmedianhigh)
    smedianhigh = discord.Embed(title='High Median', description=statistics.median_high(list(a)), color=0x00FF00)
    smedianhigh.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=smedianhigh)


"""
@math.command(pass_context=True)
async def mode(ctx,a):
    '''Find the mode (highest amount of values) of a list of numbers.\nUsage: !mode <[number1, number2, number3, ...]>\nAliases: None\nPermissions: None'''
    if a == None:
        nmode=discord.Embed(title='Error',description='Specify the numbers!',color=0xFF0000)
        nmode.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nmode)
    smode=discord.Embed(title='Mode',description=statistic.mode(list(a)),color=0x00FF00)
    smode.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    return await bot.say(embed=smode)

"""

'''
'##::::'##::::'###::::'##::: ##::::'###:::::'######:::'####:'##::: ##::'######:::                                               
 ###::'###:::'## ##::: ###:: ##:::'## ##:::'##... ##::. ##:: ###:: ##:'##... ##::                                               
 ####'####::'##:. ##:: ####: ##::'##:. ##:: ##:::..:::: ##:: ####: ##: ##:::..:::                                               
 ## ### ##:'##:::. ##: ## ## ##:'##:::. ##: ##::'####:: ##:: ## ## ##: ##::'####:                                               
 ##. #: ##: #########: ##. ####: #########: ##::: ##::: ##:: ##. ####: ##::: ##::                                               
 ##:.:: ##: ##.... ##: ##:. ###: ##.... ##: ##::: ##::: ##:: ##:. ###: ##::: ##::                                               
 ##:::: ##: ##:::: ##: ##::. ##: ##:::: ##:. ######:::'####: ##::. ##:. ######:::                                               
..:::::..::..:::::..::..::::..::..:::::..:::......::::....::..::::..:::......::::    '''


@bot.command(pass_context=True, aliases=['gr'])
async def giverole(ctx, member: discord.Member, *, role: discord.Role=None):
    '''Give a role to someone\nUsage: !giverole <member> <role>\nAliases: !gr\nPermissions: Manage Roles'''
    if not ctx.message.author.server_permissions.manage_roles:
        pgiverole = discord.Embed(title='Error', description='You don\'t have permission to give roles to members!', color=0xFF0000)
        pgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pgiverole)
    if not member:
        mgiverole = discord.Embed(title='Error', description='You must specify a member!', color=0xFF0000)
        mgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mgiverole)
    if not role:
        rgiverole = discord.Embed(title='Error', description='You must specify a role!', color=0xFF0000)
        rgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rgiverole)
    if role not in ctx.message.server.roles:
        ngiverole = discord.Embed(title='Error', description='That isn\'t a role!', color=0xFF0000)
        ngiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ngiverole)
    try:
        discord.utils.get(ctx.message.server.roles, name=role)
        await bot.add_roles(member, role)
        sgiverole = discord.Embed(title='Giverole', description=f'{ctx.message.author.mention} has given the role, {role}, to {member.name}!', color=0x00FF00)
        sgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=sgiverole)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            egiverole = discord.Embed(title='Error', description='The person you are trying to give a role to has high permissions.', color=0xFF0000)
            egiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=egiverole)
        else:
            pass


@bot.command(pass_context=True, aliases=['tr'])
async def takerole(ctx, member: discord.Member, *, role: discord.Role=None):
    '''Take a role away from someone\nUsage: !takerole <member> <role>\nAliases: !tr\nPermissions: Manage Roles'''
    if not ctx.message.author.server_permissions.manage_roles:
        ptakerole = discord.Embed(title='Error', description='You don\'t have permission to give roles to members!', color=0xFF0000)
        ptakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ptakerole)
    if not member:
        mtakerole = discord.Embed(title='Error', description='You must specify a member!', color=0xFF0000)
        mtakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mtakerole)
    if not role:
        rtakerole = discord.Embed(title='Error', description='You must specify a role!', color=0xFF0000)
        rtakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rtakerole)
    if role not in ctx.message.server.roles:
        ntakerole = discord.Embed(title='Error', description='That isn\'t a role!', color=0xFF0000)
        ntakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ntakerole)
    try:
        await bot.remove_roles(member, role)
        stakerole = discord.Embed(title='Takerole', description=f'{ctx.message.author.mention} has taken the role, {role}, from {member.name}!', color=0x00FF00)
        stakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=stakerole)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            egiverole = discord.Embed(title='Error', description=f'The person you are trying to take a role from has high permissions.', color=0xFF0000)
            egiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=egiverole)
        else:
            pass


'''
'##::::'##::'#######::'########::'########:'########:::::'###::::'########:'####::'#######::'##::: ##:                          
 ###::'###:'##.... ##: ##.... ##: ##.....:: ##.... ##:::'## ##:::... ##..::. ##::'##.... ##: ###:: ##:                          
 ####'####: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::'##:. ##::::: ##::::: ##:: ##:::: ##: ####: ##:                          
 ## ### ##: ##:::: ##: ##:::: ##: ######::: ########::'##:::. ##:::: ##::::: ##:: ##:::: ##: ## ## ##:                          
 ##. #: ##: ##:::: ##: ##:::: ##: ##...:::: ##.. ##::: #########:::: ##::::: ##:: ##:::: ##: ##. ####:                          
 ##:.:: ##: ##:::: ##: ##:::: ##: ##::::::: ##::. ##:: ##.... ##:::: ##::::: ##:: ##:::: ##: ##:. ###:                          
 ##:::: ##:. #######:: ########:: ########: ##:::. ##: ##:::: ##:::: ##::::'####:. #######:: ##::. ##:                          
..:::::..:::.......:::........:::........::..:::::..::..:::::..:::::..:::::....:::.......:::..::::..::   '''


@bot.command(pass_context=True, aliases=['k'])
async def kick(ctx, member : discord.Member=None, *, reason='The kick hammer has spoken!'):
    '''Kick someone.\nUsage: !kick <member> [reason]\nAliases: !k\nPermissions: Kick Members'''
    if not ctx.message.author.server_permissions.kick_members:
        pkick = discord.Embed(title='Error', description='You don\'t have permission to kick members!', color=0xFF0000)
        pkick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pkick)
    if not member:
        mkick = discord.Embed(title='Error', description='You must specify a member!', color=0xFF0000)
        mkick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mkick)
    if not reason:
        rkick = discord.Embed(title='Error', description='You must specify a reason!', color=0xFF0000)
        rkick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rkick)
    try:
        await bot.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            ekick = discord.Embed(title='Error', description='The person you are trying to kick has high permissions.', color=0xFF0000)
            ekick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=ekick)
        else:
            pass
    skick = discord.Embed(title='Kick', description=f'{ctx.message.author.mention} has kicked {member.name}, because: {reason}', color=0x00FF00)
    skick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=skick)
    return await bot.send_message(member, f'You have been kicked from {ctx.message.server.name} by {ctx.message.author.mention}, because {reason}', tts=True) 


@bot.command(pass_context=True, aliases=['b'])
async def ban(ctx, member : discord.Member=None, *, reason='The ban hammer has spoken!'):
    '''Ban someone\nUsage: !ban <member> [reason]\nAliases: !b\nPermissions: Ban Members'''
    if not ctx.message.author.server_permissions.ban_members:
        pban = discord.Embed(title='Error', description='You don\'t have permission to ban members!', color=0xFF0000)
        pban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pban)
    if not member:
        mban = discord.Embed(title='Error', description='You must specify a member!', color=0xFF0000)
        mban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mban)
    if not reason:
        rban = discord.Embed(title='Error', description='You must specify a reason!', color=0xFF0000)
        rban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rban)
    try:
        await bot.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            eban = discord.Embed(title='Error', description='The person you are trying to ban has high permissions.', color=0xFF0000)
            eban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=eban)
        else:
            pass
    sban = discord.Embed(title='Ban', description=f'{ctx.message.author.mention} has banned {member.name}, because: {reason}', color=0x00FF00)
    sban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=sban)
    return await bot.send_message(member, f'You have been banned from {ctx.message.server.name} by {ctx.message.author.mention}, because {reason}', tts=True) 


@bot.command(pass_context=True, aliases=['ub', 'uban'])
async def unban(ctx, member : discord.Member=None, *, reason='The unban hammer has spoken!'):
    '''Unban someone\nUsage: !unban <member> [reason]\nAliases: !ub, !uban\nPermissions: Ban Members'''
    await bot.say('Doesn\'t work, so if you have any way to fix it, look into my github. I\'ll credit ya!')
    if not ctx.message.author.server_permissions.ban_members:
        punban = discord.Embed(title='Error', description='You don\'t have permission to unban members!', color=0xFF0000)
        punban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=punban)
    if not member:
        munban = discord.Embed(title='Error', description='You must specify a member!', color=0xFF0000)
        munban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=munban)
    if not reason:
        runban = discord.Embed(title='Error', description='You must specify a reason!', color=0xFF0000)
        runban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=runban)
    try:
        banned = await bot.get_bans(ctx.message.server)
    except:
        return
    bember = discord.utils.get(banned, name=member.name)
    if bember is None:
        nunban = discord.Embed(title='Error', description=f'There isn\'t a person named {member.name} who is banned.', color=0xFF0000)
        nunban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nunban)
    await bot.unban(ctx.message.server, bember)
    sunban = discord.Embed(title='Unban', description=f'{ctx.message.author.mention} has unbanned {bember.mention}, because: {reason}', color=0x00FF00)
    sunban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=sunban)
    return await bot.send_message(member, f'You have been unbanned from {ctx.message.server.name} by {ctx.message.author.mention}, because {reason}', tts=True) 


@bot.command(pass_context=True, aliases=['sban', 'sb'])
async def softban(ctx, member : discord.Member=None, *, reason='The softban hammer has spoken!'):
    '''Ban then unban someone to remove all messages sent by the user within 7 days.\nUsage: !softban <member> [reason]\nAliases: !sban, !sb\nPermissions: Ban Members'''
    if not ctx.message.author.server_permissions.ban_members:
        psoftban = discord.Embed(title='Error', description='You don\'t have permission to softban members!', color=0xFF0000)
        psoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=psoftban)
    if not member:
        msoftban = discord.Embed(title='Error', description='You must specify a member!', color=0xFF0000)
        msoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=msoftban)
    if not reason:
        rsoftban = discord.Embed(title='Error', description='You must specify a reason!', color=0xFF0000)
        rsoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rsoftban)
    try:
        await bot.ban(member, delete_message_days=7)
        await bot.unban(discord.Server, member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            esoftban = discord.Embed(title='Error', description='The person you are trying to softban has high permissions.', color=0xFF0000)
            esoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=esoftban)
        else:
            pass
    ssoftban = discord.Embed(title='Softban', description=f'{ctx.message.author.mention} has softbanned {member.mention}, because: {reason}', color=0x00FF00)
    ssoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=ssoftban)
    return await bot.send_message(member, f'You have been softbanned from {ctx.message.server.name} by {ctx.message.author.mention}, because {reason}', tts=True) 


@bot.command(pass_context=True, aliases=['cmute', 'channelm', 'cm'])
async def channelmute(ctx, member : discord.Member, *, reason : str='The channel mute hammer has spoken!'):
    '''Mute someone in a channel.\nUsage: !channelmute <member> [reason]\nAliases: !cmute, !channelm, !cm\nPermissions: Manage Messages'''
    if not ctx.message.author.server_permissions.manage_messages:
        pchannelmute = discord.Embed(title='Error', description='You don\'t have permission to channelmute members!', color=0xFF0000)
        pchannelmute.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pchannelmute)
    if not member:
        mchannelmute = discord.Embed(title='Error', description='You must specify a member!', color=0xFF0000)
        mchannelmute.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mchannelmute)
    if not reason:
        rchannelmute = discord.Embed(title='Error', description='You must specify a reason!', color=0xFF0000)
        rchannelmute.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rchannelmute)
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
    schannelmute = discord.Embed(title='Channelmute', description=f'{ctx.message.author.mention} has channelmuted {member.mention}, because: {reason}', color=0x00FF00)
    schannelmute.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=schannelmute)
    await bot.send_message(member, f'You have been channelmuted in {ctx.message.server.name} in the {ctx.message.channel.name} channel by {ctx.message.author.mention}, because {reason}', tts=True) 


@bot.command(pass_context=True, aliases=['cumute', 'channelum', 'cunm', 'chum'])
async def channelunmute(ctx, member : discord.Member, *, reason : str='The channel mute hammer has spoken!'):
    '''Unmute someone in a channel.\nUsage: !channelunmute <member> [reason]\nAliases: !cumute,!channelum,!cunm,!chum\nPermissions: Manage Messages'''
    if not ctx.message.author.server_permissions.manage_messages:
        pchannelmute = discord.Embed(title='Error', description='You don\'t have permission to channelunmute members!', color=0xFF0000)
        pchannelmute.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pchannelmute)
    if not member:
        mchannelmute = discord.Embed(title='Error', description='You must specify a member!', color=0xFF0000)
        mchannelmute.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mchannelmute)
    if not reason:
        rchannelmute = discord.Embed(title='Error', description='You must specify a reason!', color=0xFF0000)
        rchannelmute.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rchannelmute)
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
    schannelmute = discord.Embed(title='Channelmute', description=f'{ctx.message.author.mention} has channelunmuted {member.mention}, because: {reason}', color=0x00FF00)
    schannelmute.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=schannelmute)
    await bot.send_message(member, f'You have been channelunmuted in {ctx.message.server.name} in the {ctx.message.channel.name} channel by {ctx.message.author.mention}, because {reason}', tts=True) 

@bot.command(pass_context=True)
async def warn(ctx, member : discord.Member, *, reason : str='The warn hammer has spoken!'):
    '''Warn someone about doing something wrong!\nUsage: !warn <member> [reason]\nAliases: None\nPermissions: Kick Members'''
    if not ctx.message.author.server_permissions.kick_members:
        pwarn = discord.Embed(title='Error', description='You don\'t have permission to warn members!', color=0xFF0000)
        pwarn.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pwarn)
    if not member:
        mwarn = discord.Embed(title='Error', description='You must specify a member!', color=0xFF0000)
        mwarn.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mwarn)
    if not reason:
        rwarn = discord.Embed(title='Error', description='You must specify a reason!', color=0xFF0000)
        rwarn.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rwarn)
    swarn = discord.Embed(title='Warn', description=f'{ctx.message.author.mention} has warned {member.mention}, because: {reason}', color=0x00FF00)
    swarn.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=swarn)
    await bot.send_message(member, f'You have been warned in {ctx.message.server.name} by {ctx.message.author.mention}, because {reason}', tts=True) 

@bot.command(pass_context=True)
async def purge(ctx, amount:int=None):
    '''Purge a number of messages!\nUsage: !purge <amount>\nAliases: None\nPermissions: Manage Messages'''
    if not ctx.message.author.server_permissions.manage_messages:
        ppurge = discord.Embed(title='Error', description='You don\'t have permission to purge messages!', color=0xFF0000)
        ppurge.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ppurge)
    if amount == None:
        apurge = discord.Embed(title='Error', description='You must specify an amount!', color=0xFF0000)
        apurge.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=apurge)
    await bot.purge_from(channel=ctx.message.channel, limit=amount+1)
    spurge = discord.Embed(title='Purge', description=f'{ctx.message.author.mention} has purged {amount} messages!', color=0x00FF00)
    spurge.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=spurge,delete_after=3.0)

bot.run(os.environ.get('TOKEN'))
