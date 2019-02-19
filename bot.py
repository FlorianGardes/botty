import os
import sys
import time
import random
import asyncio
import math
import re
import xlrd

import discord
from discord.utils import *
from discord.ext import commands

from datetime import datetime
from time import gmtime, strftime
import math
import datetime
from discord.ext.commands import Bot
from discord.ext import commands
from os import environ

from options_Fricen import *

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
bot = Bot(description=Description, command_prefix=CommandPrefix, pm_help = True)

# Fonctions utiles

def is_owner(ctx):
    if ctx.message.author.id == Owner_Id:
        return True
    return False

def is_channel(channel_id):
    def predicate(ctx):
        return ctx.message.channel.id == channel_id
    return commands.check(predicate)

def is_allow(ctx):
    for allowed in Allow_Id:
        if ctx.message.author.id == allowed:
            return True
    return False

# Permet de vérifier le bon lancement du bot
@bot.event
async def on_ready():
    print('--------------------------------')
    print('Bot connecté')
    print('Username : {}'.format(bot.user.name))
    print('ID : {}'.format(bot.user.id))
    print('Python Lib v{}'.format(discord.__version__))
    print('Nombre de serveur infectés:', str(len(bot.servers)))
    print('Nombre de personnes visibles:',len(set(bot.get_all_members())))
    print('--------------------------------')
    await bot.change_presence(game=(discord.Game(name='{}help'.format(CommandPrefix))))

# Message de bienvenue
@bot.event
async def on_member_join(member):
    channel = get(member.server.channels, name='nouveau-venu')
    await bot.send_message(channel,'{0.name}#{0.discriminator} à rejoins le server !'.format(member))
    await bot.send_message(member,'Bienvenue sur le serveur !\nMerci de faire !sign pseudo_IG dans le salon inscription pour acceder aux autres services\n!help pour avoir les commandes disponibles'.format(member))

@bot.command(pass_context=True, brief="Give some information about this server discord")
async def serverinfo(ctx):
    server = ctx.message.server
    online = len([m.status for m in server.members
                    if m.status == discord.Status.online or
                    m.status == discord.Status.idle])
    total_users = len(server.members)
    salons_textuels = len([x for x in server.channels
                            if x.type == discord.ChannelType.text])
    salons_vocaux = len(server.channels) - salons_textuels
    jours = (ctx.message.timestamp - server.created_at).days
    creation = ("Since {}. That's over {} days ago !""".format(server.created_at.strftime("%d %b %Y"), jours))

    data = discord.Embed(description=creation, colour=discord.Colour(value=0x206694))
    data.add_field(name="Region", value=str(server.region))
    data.add_field(name="Users Online", value="{}/{}".format(online, total_users))
    data.add_field(name="Text Channels", value=salons_textuels)
    data.add_field(name="Voice Channels", value=salons_vocaux)
    data.add_field(name="Roles", value=len(server.roles))
    data.add_field(name="Owner", value=str(server.owner))
    data.set_footer(text="Server ID: " + server.id)

    if server.icon_url:
        data.set_author(name=server.name, url=server.icon_url)
        data.set_thumbnail(url=server.icon_url)
    else:
        data.set_author(name=server.name)

    await bot.say(embed=data)

@bot.command(pass_context = True, brief="Permet de s'inscrire", description="Renome et ajoute le role à partir d'un fichier")
@is_channel(channel_inscription)
async def sign(ctx, *args):
    auteur = ctx.message.author
    prefix = ctx.message.author.name
    msg = ' '.join(args)
    wb = xlrd.open_workbook('data/Map_complet.xls')
    sh = wb.sheet_by_name(u'Map_Complet')
    colonne1 = sh.col_values(2)
    colonne2 = sh.col_values(4)
    colonne3 = sh.col_values(0)
    for rownum in range(sh.nrows):
            if(colonne1[rownum]==msg):
                role_name = colonne2[rownum]
                pseudo = colonne1[rownum]
                role = [roles.name.lower() for roles in ctx.message.server.roles]
                if (role_name.lower()) not in role:
                    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                    color = int(color, 16)
                    role = await bot.create_role(auteur.server, name=role_name, colour=discord.Colour(color))
                    await bot.add_roles(auteur, role)
                    pseudo = prefix + ' (' + pseudo +')'
                    await bot.change_nickname(ctx.message.author, pseudo)
                    embed = discord.Embed(description = "**%s** has been created and added to **%s**"%(role_name, prefix), color = 0xF00000)
                    await bot.say(embed = embed)
                    return
                role = get(ctx.message.server.roles, name=role_name)
                await bot.add_roles(auteur, role)
                pseudo = prefix + ' (' + pseudo +')'
                await bot.change_nickname(ctx.message.author, pseudo)
                embed = discord.Embed(description = "**%s** has been assigned and added to **%s**"%(role, prefix), color = 0xF00000)
                await bot.say(embed = embed)
                return
    await bot.say("Player doesn't exist, try again")

@bot.command(pass_context = True,brief="Mass message for [x/y]",hidden=True)
async def mm(ctx,*args):
    auteur = ctx.message.author
    prefix = ctx.message.author.name
    channel = discord.Object(id=message_alliance_ig)#message-alliance-ig
    channel_test = discord.Object(id=test_bot)#test-bot
    channel_message = discord.Object(id=message_alliance)#message-alliance
    if(args[0] == 'help'):
        msg ="For prepare mm (def, push or feeding), you need args like :\n!mm def x y hour quantit_of_troops feed(yes or np)\n!mm push x y hour(hh:mm:ss) quantity/player\n!mm crops x y"
        embed=discord.Embed(title="Help mass message", color=0x1ea91e)
        embed.add_field(name="Command :" , value=msg)
        embed.set_footer(text="finals.travian.com")
        embed.set_author(name=prefix)
        await bot.send_message(channel_test,embed=embed)
        return
    elif(args[0] =='def'):
        if(args[5]=='yes'):
            msg ="Hello,\n\nNeed def for [x/y]"+args[1]+"/"+args[2]+"[/x/y] pour "+args[3]+" , server time\nQuantity needed : "+args[4]+"k\nDon't forget to feed\n\nThanks in advance,\n"+prefix
            embed=discord.Embed(title="Asking def", color=0x1ea91e)
            embed.set_author(name=prefix)
            embed.set_footer(text="finals.travian.com")
            embed.add_field(name="Message : ", value=msg)


            village = "https://finals.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
            embed_discord=discord.Embed(title="Asking def wall", color=0x1ea91e)
            embed_discord.set_author(name=prefix)
            embed_discord.set_footer(text="Thank you")
            embed_discord.add_field(name="Village to def", value = village)
            embed_discord.add_field(name="Time set",value = args[3])
            embed_discord.add_field(name="Troops needed ( in k )", value = args[4])
            embed_discord.add_field(name = "Need to def ?  ", value = "Yes")
            await bot.send_message(channel,embed=embed)
            await bot.send_message(channel_message,embed=embed_discord)

        else :
            msg = "Hello warriors and amazons,\n\nNeed def in [x/y]"+args[1]+"/"+args[2]+"[/x/y] for "+args[3]+", server time\nTroops needed : "+args[4]+"k\nNo need to feed\n\nThank in advance,\n"+prefix
            embed=discord.Embed(title="Asking def wall", color=0x1ea91e)
            embed.set_author(name=prefix)
            embed.set_footer(text="finals.travian.com")
            embed.add_field(name="Message : ", value=msg)



            village = "https://finals.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
            embed_discord=discord.Embed(title="Asking Def Wall", color=0x1ea91e)
            embed_discord.set_author(name=prefix)
            embed_discord.set_footer(text="Thank you")
            embed_discord.add_field(name="Village to def", value = village)
            embed_discord.add_field(name="Time set",value = args[3])
            embed_discord.add_field(name="Troops needed ( in k ) ", value = args[4])
            embed_discord.add_field(name = "Need to feed ? ", value = "No")
            await bot.send_message(channel,embed=embed)
            await bot.send_message(channel_message,embed=embed_discord)
    elif(args[0]=='push'):
        msg = "Hello everyone,\n\nPush in [x/y]"+args[1]+"/"+args[2]+"[/x/y] until "+args[3]+" , server time\n"+args[4]+"k/player asked\n\nThank you in advance,\n"+prefix
        embed=discord.Embed(title="Push", color=0x1ea91e)
        embed.set_author(name=prefix)
        embed.set_footer(text="finals.travian.com")
        embed.add_field(name="Message : ", value=msg)

        village = "https://finals.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
        embed_discord=discord.Embed(title="Push", color=0x1ea91e)
        embed_discord.set_author(name=prefix)
        embed_discord.set_footer(text="Thank you")
        embed_discord.add_field(name="Village to push", value = village)
        embed_discord.add_field(name="Hour",value = args[3])
        embed_discord.add_field(name="Quantity asked ( in k )", value = args[4])
        await bot.send_message(channel,embed=embed)
        await bot.send_message(channel_message,embed=embed_discord)

    elif(args[0]=='crops'):
        msg = "Hello everyone,\n\nDon't forget to feed in [x/y]"+args[1]+"/"+args[2]+"[/x/y],\nThank you in advance\n"+prefix
        embed=discord.Embed(title="Crops", color=0x1ea91e)
        embed.set_author(name=prefix)
        embed.set_footer(text="finals.travian.com")
        embed.add_field(name="Need crops : ", value=msg)

        village = "https://finals.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
        embed_discord=discord.Embed(title="Push", color=0x1ea91e)
        embed_discord.set_author(name=prefix)
        embed_discord.set_footer(text="Thank you")
        embed_discord.add_field(name="Village to feed", value = village)
        await bot.send_message(channel,embed=embed)
        await bot.send_message(channel_message,embed=embed_discord)

@bot.command(pass_context = True, hidden=True,brief="Créé un role")
async def createrole(ctx, *args):
    role = [roles.name.lower() for roles in ctx.message.author.roles]
    if 'dev' not in role:
        return await bot.say("**Désolé tu n'es pas autorisé à faire cette commande!**")
    msg = ' '.join(args)
    auteur = ctx.message.author
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    role = await bot.create_role(auteur.server, name=msg, colour=discord.Colour(color))
    await bot.say('Role créé avec succes par %s'%auteur )

@bot.command(pass_context = True, brief="Info player")
async def info(ctx ,*args):
    auteur = ctx.message.author
    prefix = ctx.message.author.name
    msg = ' '.join(args)
    wb = xlrd.open_workbook('data/Map_complet.xls')
    sh = wb.sheet_by_name(u'Map_Complet')
    colonne1_id = sh.col_values(1)
    colonne1 = sh.col_values(2)
    colonne2_id = sh.col_values(3)
    colonne2 = sh.col_values(4)
    for rownum in range (sh.nrows):
        if(colonne1[rownum]==msg):
            embed = discord.Embed(title="Information", color=0xff8c00)
            joueur = "https://finals.travian.com/spieler.php?aid=%d" %(int(colonne1_id[rownum]))
            alliance = "https://finals.travian.com/allianz.php?aid=%d" %(int(colonne2_id[rownum]))
            embed.add_field(name =msg,value =joueur)
            embed.add_field(name = colonne2[rownum], value = alliance)
            await bot.say(embed=embed)
            return
    await bot.say("Player doesn't exist")

@bot.command(pass_context = True, brief ="Link")
async def link():
    embed = discord.Embed(title="Link", color=0xff8c00)
    embed.add_field(name ="Server",value ="https://finals.travian.com")
    embed.add_field(name ="Getter",value ="https://www.gettertools.com/finals.travian.com.9/")
    embed.add_field(name ="TW WW",value ="http://www.travianwonder.com/uollasww")
    embed.add_field(name ="Kirilloid",value ="http://travian.kirilloid.ru/")
    await bot.say(embed=embed)

@bot.command(pass_context=True, brief="Sent an invitation in pm of the server", aliases=['inv'])
async def invite(ctx):
    channel = discord.Object(id=channel_bienvenue)
    auteur = ctx.message.author
    server = ctx.message.server
    link = await bot.create_invite(destination = channel, temporary = False, max_uses = 1)
    embedmp = discord.Embed(color=0xf41af4)
    embedmp.add_field(name="Discord invitation link:", value=link)
    embedmp.set_footer(text="%s invited link"%server)
    embed = discord.Embed(description ="Invitation sent in Private Message to **%s**"%auteur, color=0xf41af4)
    await bot.delete_message(ctx.message)
    await bot.send_message(ctx.message.channel, embed=embed)
    await bot.send_message(auteur, embed=embedmp)

@bot.command()
async def ping(*args):
	await bot.say(':ping_pong: Pong!')

@bot.command()
async def tuturu(*args):
	await bot.say('\o/')

@bot.command(brief="Give date & hour")
async def time(*args):
	await bot.say(' :timer: ' + strftime('We are the %d-%m-%Y and it is %H:%M:%S'))

# Kick un membre du serveur
@bot.command(pass_context = True, hidden=True)
async def kick(ctx, *, member : discord.Member = None):
    role = [roles.name.lower() for roles in ctx.message.author.roles]

    if 'admin' not in role:
        return await bot.say("**Désolé tu n'es pas autorisé à faire cette commande!**")
    if not member:
        return await bot.say(ctx.message.author.mention + ", veuillez préciser le membre à kick")
    embed = discord.Embed(description = "**%s** à été kick"%member.name, color = 0xF00000)
    embed.set_footer(text="Bye bye")
    await bot.kick(member)
    await bot.say(embed = embed)

# Supprime le message pour ne laisser que la commande
@bot.command(pass_context = True, hidden=True)
@commands.check(is_owner)
async def delcmd(ctx, *args):
    msg = ' '.join(args)
    await bot.delete_message(ctx.message)
    await bot.say(msg)

@bot.command(pass_context = True, hidden=True)
@commands.check(is_allow)
async def clear(ctx, lignes):
    mgs = []
    lignes = int(lignes)
    async for x in bot.logs_from(ctx.message.channel, limit = lignes+1):
        mgs.append(x)
    await bot.delete_messages(mgs)
    embed = discord.Embed(description = "**%s** message(s) supprimé(s) par **%s**"%(lignes, ctx.message.author), color = 0xF00000)
    embed.set_footer(text="Clear")
    await bot.say(embed = embed)

@bot.command(pass_context = True, hidden=True)
async def test(ctx, *args):
    embed = discord.Embed(description = "test", color = 0xF00000)
    author = ctx.message.author.name
    embed.set_author(name=author)
    await bot.say(embed = embed)

bot.run(Token_Fricen)
