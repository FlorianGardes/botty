#!/usr/bin/python3
#import os
#import sys
#import requests
#import datetime
import discord

from discord.ext import commands, tasks

from options_fricen import *

#from extensions.travian import travian
#from extensions.fun import fun
#from extensions.serveur import serveur

#bot = commands.Bot(description=Description, command_prefix=CommandPrefix, pm_help = True)

def get_prefix(client, message):
    prefixes = CommandPrefix
    return commands.when_mentioned_or(*prefixes)(client, message)

class Botty(commands.Bot):
        
        def __init__(self):
            super().__init__(
                command_prefix=CommandPrefix,
                description=Description,
                pm_help = True,
            )
                
       	    self.load_extension("extensions.fun")
       	    self.load_extension("extensions.serveur")
            self.load_extension("extensions.travian")
        
        async def on_ready(self):
            print('--------------------------------')
            print('Bot connecté')
            print('Username : {}'.format(self.bot.user.name))
            print('ID : {}'.format(self.bot.user.id))
            print('discord.py v{}'.format(discord.__version__))
            print('Nombre de serveur infectés:', str(len(self.bot.servers)))
            print('Nombre de personnes visibles:',len(set(self.bot.get_all_members())))
            print('--------------------------------')
            await self.bot.change_presence(game=(discord.Game(name='{}help'.format(CommandPrefix))))
        
        def run(self):
            super().run(self.config[Token_Fricen])

bot = Botty()
bot.run()
