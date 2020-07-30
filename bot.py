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
    print('--------------------------------')

@bot.event
async def on_message(message):
    if message.channel.id != channel_inscription:
        await bot.process_commands(message)
    if message.author == bot.user: #immunité au bot
        return
    if message.channel.id == channel_inscription:
        message_content = message.content
        sign_message = message_content[:5]
        channel = message.channel
        if sign_message != '$sign':
            await message.delete()
            await channel.send("**%s**"%(str(message.author)) +", use the `$sign` command please!")
        else:
            await bot.process_commands(message)

bot.run(Token_Fricen)
