import os
import sys
import random
import asyncio
import math
import re
import requests
import xlrd
import cogs

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

cogs_list = [cogs.Travian,
             cogs.Serveur,
             cogs.Fun]

for cog in cogs_list:
        bot.add_cog(cog(bot))

bot.run(Token_Fricen)
