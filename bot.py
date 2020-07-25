#!/usr/bin/python3
#import os
#import sys
#import random
#import asyncio
#import math
#import re
#import requests
#import datetime
#import xlrd

import discord
from discord.ext import commands, tasks

from options_fricen import *

#from extensions.travian import travian
#from extensions.fun import fun
#from extensions.serveur import serveur

bot = commands.Bot(description=Description, command_prefix=CommandPrefix, pm_help = True)


bot.load_extension("extensions.fun")
bot.load_extension("extensions.serveur")
bot.load_extension("extensions.travian")
    
@bot.event  
async def on_ready():
    print('--------------------------------')
    print('Bot connecté')
    print('Username : {}'.format(bot.user.name))
    print('ID : {}'.format(bot.user.id))
    print('discord.py v{}'.format(discord.__version__))
    #print('Nombre de serveur infectés:', str(len(bot.servers)))
    #print('Nombre de personnes visibles:',len(set(bot.get_all_members())))
    print('--------------------------------')
    #await bot.change_presence(game=(discord.Game(name='{}help'.format(CommandPrefix))))
      
bot.run(Token_Fricen)
