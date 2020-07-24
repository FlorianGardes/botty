import discord
import asyncio
import random
import time
import datetime
from time import gmtime, strftime
from discord.ext import commands
from options_fricen import *
from discord.utils import *

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, *args):
    	await self.bot.say(':ping_pong: Pong!')

    @commands.command()
    async def tuturu(self, *args):
    	await self.bot.say('\o/')

    @commands.command()
    async def time(self, *args):
    	await self.bot.say(':timer: ' + strftime('We are the %d-%m-%Y and it is %H:%M:%S'))

def setup(bot):
    bot.add_cog(fun(bot))
