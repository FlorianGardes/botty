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

from options_ghosty import *

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
bot = commands.Bot(description=Description, command_prefix=CommandPrefix, pm_help = True)

try:
    bot.load_extension("cogs.travian")
except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

# Fonctions utiles

def is_owner(ctx):
    if ctx.message.author.id == Owner_Id:
        return True
    return False

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

@bot.command(pass_context=True, aliases=['inv'], description="Sent invitation")
async def invite(ctx):
    """Sent an invitation in pm of the server"""
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

bot.run(Token)
