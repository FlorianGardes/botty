import os
import sys
import time
import random
import asyncio
import math
import re

import discord

from datetime import datetime
from time import gmtime, strftime
import math
import datetime
from discord.ext.commands import Bot
from discord.ext import commands
from os import environ

from options import *

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Botty le bot", command_prefix=CommandPrefix, pm_help = True)

# Permet de vérifier le bon lancement du bot
@client.event
async def on_ready():
    print("Client connecté")
    print("Username : {}".format(client.user.name))
    print("ID : {}".format(client.user.id))
    print("discord.py v{}".format(discord.__version__))
    await client.change_presence(game=(discord.Game(name='{}help'.format(environ.get(CommandPrefix)))))

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):
	await client.say(":ping_pong: Pong!")
# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.

@client.command()
async def hi(*args):
	await client.say("HOI o/")

@client.command()
async def time(*args):
	await client.say(" :timer: " + strftime("On est le %d-%m-%Y et il est %H:%M:%S"))

client.run(Token)
