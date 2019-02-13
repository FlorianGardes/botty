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
client = Bot(description=Description, command_prefix=CommandPrefix, pm_help = True)

# Fonctions utiles

def is_owner(ctx):
    if ctx.message.author.id == Owner_Id:
        return True
    return False

def is_allowed(ctx):
    if is_owner(ctx):
        return True
    else:
        return False

# Permet de vérifier le bon lancement du bot
@client.event
async def on_ready():
    print("Client connecté")
    print("Username : {}".format(client.user.name))
    print("ID : {}".format(client.user.id))
    print("discord.py v{}".format(discord.__version__))
    await client.change_presence(game=(discord.Game(name='{}help'.format(CommandPrefix))))

# Message de bienvenue
@client.event
async def on_member_join(member):
    await client.send_message(member,"Bienvenue sur le serveur Ghosty {0.name}#{0.discriminator} ! :ghost: ".format(member))
    channel = get(member.server.channels, name="bienvenue")
    await client.send_message(channel,"Bienvenue à {0.name} ! :eggplant: ".format(member))

@client.command()
async def ping(*args):
	await client.say(":ping_pong: Pong!")

@client.command()
async def hi(*args):
	await client.say("coucou o/")

@client.command()
async def time(*args):
	await client.say(" :timer: " + strftime("On est le %d-%m-%Y et il est %H:%M:%S"))

@client.command()
async def mm(*args):
    if(args[0] == "coa"):
        if(args [1] == "push"):
            await client.say (" Push coa en [x/y]"+args[2]+"[/x/y]")
'''
@client.command()
async def ally(*args):
    if(args[0]) == "fhc" or (args[0]) == "FHC":
        role = get(message.server.roles, name='FHC')
        await client.add_roles(message.author, role)
'''
'''
@client.command(pass_context=True)
@client.check(is_owner)
async def ban(ctx, user : discord.Member):
    await client.ban(user)
    await client.say("{0.name} a été banni !".format(user))
'''
'''
@client.command(pass_context=True)
@client.check(is_owner)
async def ban(ctx, user: discord.Member):
        if (message.author == message.server.owner):
            await client.ban(user)
            await client.say(f"{user.name} à été ban !")
        else:
            await client.send_message(message.channel, "Commande uniquement pour le créateur tout puissant")
'''
client.run(Token)
