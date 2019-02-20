import os
import sys
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

from options_fricen import *

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
bot = commands.Bot(description=Description, command_prefix=CommandPrefix, pm_help = True)

try:
    bot.load_extension("cogs.travian")
    bot.load_extension("cogs.serveur")
    bot.load_extension("cogs.fun")
except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print(_("Failed to load extension {}\n{}").format(extension, exc))

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
    print('discord.py v{}'.format(discord.__version__))
    print('Nombre de serveur infectés:', str(len(bot.servers)))
    print('Nombre de personnes visibles:',len(set(bot.get_all_members())))
    print('--------------------------------')
    await bot.change_presence(game=(discord.Game(name='{}help'.format(CommandPrefix))))

# Supprime le message pour ne laisser que la commande
@bot.command(pass_context = True, hidden=True)
@commands.check(is_owner)
async def delcmd(ctx, *args):
    msg = ' '.join(args)
    await bot.delete_message(ctx.message)
    await bot.say(msg)

@bot.command(pass_context = True, hidden=True)
async def test(ctx, *args):
    embed = discord.Embed(description = "test", color = 0xF00000)
    author = ctx.message.author.name
    embed.set_author(name=author)
    await bot.say(embed = embed)

bot.run(Token)
