import discord
from discord.ext import commands
import os
import time
import random
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
        hhelp.add_field(name='Informational', value='`cryptocurrency` `calculate`')
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
        ssuggest = discord.Embed(title='Suggest',description='Sent that suggestion over! Thank you!',color=0x00FF00)
        ssuggest.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.send_message(destination=ctx.message.channel,embed=ssuggest)
        reactionmessage = await bot.send_message(discord.Object(id='431958602148872222'),embed=osuggest)
        await bot.add_reaction(reactionmessage, '✅')
        await bot.add_reaction(reactionmessage, '❌')
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

@bot.command(pass_context=True, aliases=['math'])
async def calculate(ctx, expression):
    '''Work out expressions and equations.\nUsage: !calculate <expression>\nAliases: !math\nPermissions: None'''
    r = requests.get('http://api.mathjs.org/v4/?expr=' + expression)
    text = r.text
    if r.status_code == 200:
        if expression == None:
            ncalculate = discord.Embed(title='Error', description='Specify the expression!', color=0xFF0000)
            ncalculate.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=ncalculate)
        if expression:
            scalculate = discord.Embed(title='Expression', description='{}'.format(expression), color=0x00FF00)
            scalculate.add_field(name='Answer', value='Your answer is: ' + text)
            scalculate.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=scalculate)
        else:
            return
    if r.status_code == 400:
        icalculate = discord.Embed(title='Error', description='That is an invalid expression!', color=0xFF0000)
        icalculate.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=icalculate)
    else:
        rcalculate = discord.Embed(title='Error', description='I could not access the API! Direct Message Pointless#1278 so this can be fixed! (You will be credited for finding it out!)', color=0xFF0000)
        rcalculate.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rcalculate)



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
    sserverinfo = discord.Embed(title = (str(ctx.message.server.name)),colour=0x00FF00)
    sserverinfo.set_thumbnail(url = ctx.message.server.icon_url)
    sserverinfo.add_field(name='Owner', value=str(ctx.message.server.owner))
    sserverinfo.add_field(name ='ID', value=str(ctx.message.server.id))
    sserverinfo.add_field(name ='Member Count', value=str(ctx.message.server.member_count))
    sserverinfo.add_field(name ='Region', value=str(ctx.message.server.region))
    sserverinfo.add_field(name ='AFK Timeout', value=str(ctx.message.server.afk_timeout))
    sserverinfo.add_field(name ='AFK Channel', value=str(ctx.message.server.afk_channel))
    sserverinfo.add_field(name ='Verification Level',value=str(ctx.message.server.verification_level))
    sserverinfo.add_field(name ='Custom Emotes',value=len(ctx.message.server.emojis))
    sserverinfo.add_field(name ='Channels',value=len(ctx.message.server.channels))
    sserverinfo.add_field(name ='Features',value=str(ctx.message.server.features))
    sserverinfo.set_footer(text =f'Created at: {str(ctx.message.server.created_at)}')
    await bot.say(embed=sserverinfo)
'''
@bot.command(pass_context=True)
async def userinfo(ctx,user:str=ctx.message.author):
    'See information about a user!\nUsage: !userinfo [user]\nAliases: None\nPermissions: None'
    suserinfo = discord.Embed(title = (str(ctx.message.server.name)),color=0x00FF00)
    suserinfo.set_thumbnail(url = ctx.message.author.icon_url)
    suserinfo.add_field(name='')
    await bot.say(embed=suserinfo)
'''
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
    if role == None:
        nogiverole = discord.Embed(title='Error', description='That isn\'t a role!', color=0xFF0000)
        nogiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=nogiverole)
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
