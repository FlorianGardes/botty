#!/usr/bin/python3
import os
import sys
import requests
import datetime

import discord
from discord.utils import *
from discord.ext import commands

from options_fricen import *
import extensions
from extensions import travian
from extensions import fun
from extensions import serveur

bot = commands.Bot(description=Description, command_prefix=CommandPrefix, pm_help = True)

cogs_list = [extensions.Travian,
             extensions.Serveur,
             extensions.Fun]

# Permet de vérifier le bon lancement du bot
@bot.event
async def on_ready():
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
                
        await bot.change_presence(game=(discord.Game(name='{}help'.format(CommandPrefix))))

bot.run(Token_Fricen)
