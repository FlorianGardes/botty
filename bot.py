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

# Fonctions utiles
'''
def is_owner(ctx):
    if ctx.message.author.id == Owner_Id:
        return True
    return False
'''

bot.run(Token_Fricen)
