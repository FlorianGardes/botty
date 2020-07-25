#!/usr/bin/python3
import os
import sys
import requests
import datetime
import discord
import logging
import aiohttp

from discord.ext import commands

from options_fricen import *

from extensions.travian import travian
from extensions.fun import fun
from extensions.serveur import serveur

#bot = commands.Bot(description=Description, command_prefix=CommandPrefix, pm_help = True)

log = logging.getLogger(__name__)

initial_extensions = (
        'extensions.travian',
        'extensions.fun',
        'extensions.serveur',
)

class Botty():
    def __init__(self):
        super().__init__(command_prefix=CommandPrefix, description=Description, pm_help = True)
        
        self.client_id = config.client_id
        self.session = aiohttp.ClientSession(loop=self.loop)
        
        for extension in initial_extensions:
                try:
                        self.load_extension(extension)
                except Exception as e:
                        print(f'Failed to load extension {extension}.', file=sys.stderr)
                        traceback.print_exc()
                        
    async def close(self):
        await super().close()
        await self.session.close()
        
    def run(self):
        try:
            super().run(config.Token_Fricen, reconnect=True)

    @property
    def config(self):
        return __import__('config')
