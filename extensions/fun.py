from time import gmtime, strftime
import discord
from discord.ext import commands
from options_fricen import *

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
    	await ctx.send(':ping_pong: Pong!')

    @commands.command()
    async def tuturu(self, ctx):
    	await ctx.send('\o/')

    @commands.command()
    async def time(self, ctx):
    	await ctx.send(':timer: ' + strftime('We are the %d-%m-%Y and it is %H:%M:%S'))

def setup(bot):
        bot.add_cog(fun(bot))
