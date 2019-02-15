import os
import sys
import time
import random
import asyncio
import math
import re
import requests

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
    await bot.send_message(member,'Bienvenue sur le serveur Ghosty {0.name}#{0.discriminator} ! :ghost: '.format(member))
    channel = get(member.server.channels, name='bienvenue')
    await bot.send_message(channel,'Bienvenue à {0.name} ! :eggplant: '.format(member))

@bot.command()
async def ping(*args):
	await bot.say(':ping_pong: Pong!')

@bot.command()
async def tuturu(*args):
	await bot.say('\o/')

@bot.command()
async def time(*args):
	await bot.say(' :timer: ' + strftime('On est le %d-%m-%Y et il est %H:%M:%S'))

@bot.command()
async def mm(*args):
    if(args[0] == 'coa'):
        if(args [1] == 'push'):
            await bot.say (' Push coa en [x/y]'+args[2]+'[/x/y]')

@bot.command(pass_context = True)
async def ally(ctx, *args):
    msg = ' '.join(args)
    auteur = ctx.message.author
    if msg == 'fhc' or msg == 'FHC':
        role = get(ctx.message.server.roles, name='FHC')
        await bot.add_roles(auteur, role)
    elif msg == 'G&V' or msg == 'g&v':
        role = get(ctx.message.server.roles, name='G&V')
        await bot.add_roles(auteur, role)
    await bot.say('Role %s ajouté pour %s'%(role, auteur) )


@bot.command(pass_context = True)
@commands.check(is_owner)
async def delcmd(ctx, *args):
    msg = ' '.join(args)
    await bot.delete_message(ctx.message)
    await bot.say(msg)

@bot.command(pass_context = True)
async def test(ctx, *args):
    msg = ' '.join(args)
    await bot.say(ctx.message.content)
    await bot.say(msg)

bot.run(Token)
