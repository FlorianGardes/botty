import os
import sys
import time
import random
import asyncio
import math
import re
import requests
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

from options import *

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
    #await bot.send_message(member,'Bienvenue sur le serveur Ghosty {0.name}#{0.discriminator} ! :ghost: '.format(member))
    channel = get(member.server.channels, name='bienvenue')
    await bot.send_message(channel,'Bienvenue à {0.name} ! :eggplant: '.format(member))

@bot.command(pass_context=True, brief="Donne quelques informations sur le serveur")
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
    creation = ("Depuis le {}. Il s'est écoulé {} jours !""".format(server.created_at.strftime("%d %b %Y"), jours))

    data = discord.Embed(description=creation, colour=discord.Colour(value=0x206694))
    data.add_field(name="Region", value=str(server.region))
    data.add_field(name="Utilisateurs en ligne", value="{}/{}".format(online, total_users))
    data.add_field(name="Salons Textuels", value=salons_textuels)
    data.add_field(name="Salon Vocaux", value=salons_vocaux)
    data.add_field(name="Roles", value=len(server.roles))
    data.add_field(name="Propriétaire", value=str(server.owner))
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
                role = [roles.name.lower() for roles in ctx.message.author.roles]
                if (role_name.lower()) not in role:
                    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                    color = int(color, 16)
                    role = await bot.create_role(auteur.server, name=role_name, colour=discord.Colour(color))
                    await bot.add_roles(auteur, role)
                    pseudo = prefix + ' (' + pseudo +')'
                    await bot.change_nickname(ctx.message.author, pseudo)
                    embed = discord.Embed(description = "**%s** à été créé et ajouté à **%s**"%(role_name, prefix), color = 0xF00000)
                    if(colonne3[rownum]==1):
                        embed.set_footer(text=":romain:")
                    elif(colonne3[rownum]==2):
                        embed.set_footer(text=":germain:")
                    else :
                        embed.set_footer(text=":gaulois:")
                    await bot.say(embed = embed)
                    return
                role = get(ctx.message.server.roles, name=role_name)
                await bot.add_roles(auteur, role)
                pseudo = prefix + ' (' + pseudo +')'
                await bot.change_nickname(ctx.message.author, pseudo)
                embed = discord.Embed(description = "**%s** à été attribué et ajouté à **%s**"%(role, prefix), color = 0xF00000)
                if(colonne3[rownum]==1):
                    embed.set_footer(text=":romain:")
                elif(colonne3[rownum]==2):
                    embed.set_footer(text=":germain:")
                else :
                    embed.set_footer(text=":gaulois:")
                await bot.say(embed = embed)
                return
    await bot.say("Pseudo introuvable")

@bot.command(brief="Demande de push en [x/y]")
async def mm(*args):
    channel = discord.Object(id=message_alliance_ig)#message-alliance-ig
    channel_test = discord.Object(id=test_bot)#test-bot
    channel_message = discord.Object(id=message_alliance)#message-alliance
    if(args[0] == 'help'):
        msg ="Veuillez spécifiez si c'est un message def ou push comme suit :\n!mm def x y heure troupe_total nourrir(oui ou non)\n!mm push x y heure quantité_par_joueurs"
        embed=discord.Embed(title="Help message alliance", color=0x1ea91e)
        embed.add_field(name="Commande :" , value=msg)
        embed.set_footer(text="finals.travian.com")
        embed.set_author(name="Fricen")
        await bot.send_message(channel_test,embed=embed)
        return
    elif(args[0] =='def'):
        if(args[5]=='oui'):
            msg ="Bonjour à tous,\n\nBesoin de def en [x/y]"+args[1]+"/"+args[2]+"[/x/y] pour "+args[3]+" heure, heure serveur\nQuantité demandées : "+args[4]+"k\nPensez à nourrir\n\nMerci d'avance,\nFricen"
            embed=discord.Embed(title="Demande de def", color=0x1ea91e)
            embed.set_author(name="Fricen")
            embed.set_footer(text="finals.travian.com")
            embed.add_field(name="Coord : ", value=msg)


            village = "https://finals.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
            embed_discord=discord.Embed(title="Demande de def", color=0x1ea91e)
            embed_discord.set_author(name="Fricen")
            embed_discord.set_footer(text="Merci")
            embed_discord.add_field(name="Village à défendre", value = village)
            embed_discord.add_field(name="Heure d'impact",value = args[3])
            embed_discord.add_field(name="Quantité demandée en k", value = args[4])
            embed_discord.add_field(name = "Besoin de nourrir ? ", value = "Oui")
            await bot.send_message(channel,embed=embed)
            await bot.send_message(channel_message,embed=embed_discord)

        else :
            msg = "Bonjour à tous,\n\nBesoin de def en [x/y]"+args[1]+"/"+args[2]+"[/x/y] pour "+args[3]+"heure, heure serveur\nQuantité demandées : "+args[4]+"k\nPas besoin de nourrir\n\nMerci d'avance,\nFricen"
            embed=discord.Embed(title="Demande de def", color=0x1ea91e)
            embed.set_author(name="Fricen")
            embed.set_footer(text="finals.travian.com")
            embed.add_field(name="Coord : ", value=msg)



            village = "https://finals.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
            embed_discord=discord.Embed(title="Demande de def", color=0x1ea91e)
            embed_discord.set_author(name="Fricen")
            embed_discord.set_footer(text="Merci")
            embed_discord.add_field(name="Village à défendre", value = village)
            embed_discord.add_field(name="Heure d'impact",value = args[3])
            embed_discord.add_field(name="Quantité demandée en k", value = args[4])
            embed_discord.add_field(name = "Besoin de nourrir ? ", value = "Non")
            await bot.send_message(channel,embed=embed)
            await bot.send_message(channel_message,embed=embed_discord)
    elif(args[0]=='push'):
        msg = "Bonjour à tous,\n\nPush en [x/y]"+args[1]+"/"+args[2]+"[/x/y] jusqu'à "+args[3]+" heure, heure serveur\n"+args[4]+"k par joueurs\n\nMerci d'avance,\nFricen"
        embed=discord.Embed(title="Demande de Push", color=0x1ea91e)
        embed.set_author(name="Fricen")
        embed.set_footer(text="finals.travian.com")
        embed.add_field(name="Coord : ", value=msg)

        village = "https://finals.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
        embed_discord=discord.Embed(title="Demande de def", color=0x1ea91e)
        embed_discord.set_author(name="Fricen")
        embed_discord.set_footer(text="Merci")
        embed_discord.add_field(name="Village à push", value = village)
        embed_discord.add_field(name="Heure",value = args[3])
        embed_discord.add_field(name="Quantité demandée en k", value = args[4])
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

@bot.command(pass_context = True,brief="Info player")
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
    await bot.say("Pseudo introuvable")

@bot.command()
async def ping(*args):
	await bot.say(':ping_pong: Pong!')

@bot.command()
async def tuturu(*args):
	await bot.say('\o/')

@bot.command(brief="Affiche la date et l'heure")
async def time(*args):
	await bot.say(' :timer: ' + strftime('On est le %d-%m-%Y et il est %H:%M:%S'))

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
    #msg = ' '.join(args)
    await bot.say(ctx.message.content)
    await bot.say(args[0])
    await bot.say(args[1])
    await bot.say(args[2])

bot.run(Token)
