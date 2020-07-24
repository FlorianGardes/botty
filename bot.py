#!/usr/bin/python3
import os
import sys
import random
import asyncio
import math
import re
import requests
import xlrd
import extensions

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

cogs_list = [extensions.Travian,
             extensions.Serveur,
             extensions.Fun]

# Permet de vérifier le bon lancement du bot
@bot.event
async def on_ready(self):
        print('--------------------------------')
        print('Bot connecté')
        print('Username : {}'.format(self.bot.user.name))
        print('ID : {}'.format(self.bot.user.id))
        print('discord.py v{}'.format(discord.__version__))
        print('Nombre de serveur infectés:', str(len(self.bot.servers)))
        print('Nombre de personnes visibles:',len(set(self.bot.get_all_members())))
        print('--------------------------------')
        
        for cog in cogs_list:
                bot.add_cog(cog(bot))
                
        await self.bot.change_presence(game=(discord.Game(name='{}help'.format(CommandPrefix))))

bot.run(Token_Fricen)
