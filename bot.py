#!/usr/bin/python3
import os
import sys
import requests
import datetime
import discord
import logging
import aiohttp
import asyncpg

from discord.ext import commands

from options_fricen import *

from extensions.travian import travian
from extensions.fun import fun
from extensions.serveur import serveur

bot = commands.Bot(description=Description, command_prefix=CommandPrefix, pm_help = True)

log = logging.getLogger(__name__)

initial_extensions = (
        'extensions.travian',
        'extensions.fun',
        'extensions.serveur',
)

class Botty():
    def __init__(self):
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
                for extension in initial_extensions:
                        try:
                                self.load_extension(extension)
                        except Exception as e:
                                print(f'Failed to load extension {extension}.', file=sys.stderr)
                                traceback.print_exc()
                await self.bot.change_presence(game=(discord.Game(name='{}help'.format(CommandPrefix))))

bot.run(Token_Fricen)
