import discord
import asyncio
import xlrd
import xlwt
import random
from discord.ext import commands
from options_fricen import *
from discord.utils import *

def is_channel(channel_id):
    def predicate(ctx):
        return ctx.message.channel.id == channel_id
    return commands.check(predicate)

async def is_allow(ctx):
    for allowed in Allow_Id:
        if ctx.author.id == allowed:
            return True
    return False

async def is_owner(ctx):
        return ctx.author.id == Owner_Id

async def sign_manual(self, entire_pseudo_bot, pseudo_discord, pseudo_ig, ctx):
    auteur = entire_pseudo_bot
    prefix = entire_pseudo_bot.name
    msg = pseudo_ig
    wb = xlrd.open_workbook('data/Map_Complet.xls')
    sh = wb.sheet_by_name(u'Map_Complet')
    colonne1 = sh.col_values(2)
    colonne2 = sh.col_values(4)
    colonne3 = sh.col_values(0)
    for rownum in range(sh.nrows):
        if(colonne1[rownum]==msg):
            role_name = colonne2[rownum]
            pseudo = colonne1[rownum]
            role = [roles.name.lower() for roles in ctx.message.guild.roles]
            if (role_name.lower()) not in role:
                color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                color = int(color, 16)
                role = await ctx.guild.create_role(name=role_name, colour=discord.Colour(color))
                await auteur.add_roles(role)
                pseudo = prefix + ' (' + pseudo +')'
                await auteur.edit(nick=pseudo)
                embed = discord.Embed(description = "**%s** has been created and added to **%s**"%(role_name, prefix), color = 0xF00000)
                await ctx.send(embed = embed)
                return
            role = get(ctx.message.guild.roles, name=role_name)
            await auteur.add_roles(role)
            pseudo = prefix + ' (' + pseudo +')'
            await auteur.edit(nick=pseudo)
            embed = discord.Embed(description = "**%s** has been assigned and added to **%s**"%(role, prefix), color = 0xF00000)
            await ctx.send(embed = embed)
            return
    await ctx.send("Player doesn't exist, try again")

class travian(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    @is_channel(channel_inscription)
    async def sign(self, ctx, *args):
        """Allows to register
        Use it with your own Travian nickname like $sign <Travian nickname>
        """
        auteur = ctx.message.author
        prefix = ctx.message.author.name
        msg = ' '.join(args)
        if msg == '':
            await ctx.send('Please enter your Travian nickname after `$sign`')
            return
        wb = xlrd.open_workbook('data/Map_Complet.xls')
        sh = wb.sheet_by_name(u'Map_Complet')
        colonne1 = sh.col_values(2)
        colonne2 = sh.col_values(4)
        colonne3 = sh.col_values(0)
        for rownum in range(sh.nrows):
                if(colonne1[rownum]==msg):
                    role_name = colonne2[rownum]
                    pseudo = colonne1[rownum]
                    role = [roles.name.lower() for roles in ctx.message.guild.roles]
                    if (role_name.lower()) not in role:
                        color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                        color = int(color, 16)
                        role = await ctx.guild.create_role(name=role_name, colour=discord.Colour(color))
                        await ctx.author.add_roles(role)
                        pseudo = prefix + ' (' + pseudo +')'
                        await ctx.author.edit(nick=pseudo)
                        embed = discord.Embed(description = "**%s** has been created and added to **%s**"%(role_name, prefix), color = 0xF00000)
                        await ctx.send(embed = embed)
                        return
                    role = get(ctx.message.guild.roles, name=role_name)
                    await ctx.author.add_roles(role)
                    pseudo = prefix + ' (' + pseudo +')'
                    await ctx.author.edit(nick=pseudo)
                    embed = discord.Embed(description = "**%s** has been assigned and added to **%s**"%(role, prefix), color = 0xF00000)
                    await ctx.send(embed = embed)
                    return
        await ctx.send("Player doesn't exist, try again")


    @commands.command(pass_content = True, hidden=True)
    @commands.check(is_allow)
    async def signadmin(self, ctx, *args):
        entire_pseudo = ' '.join(args)
        pseudo_discord = entire_pseudo[:-5]
        entire_pseudo = int(entire_pseudo)
        entire_pseudo_bot = ctx.guild.get_member(entire_pseudo)
        prefix = entire_pseudo_bot.name
        await ctx.message.delete()
        embed = discord.Embed(title="%s"%(entire_pseudo), color=0xF00000)
        embed.add_field(name = "Pseudo discord: ",value =prefix)
        embed.set_footer(text = "Please, enter Travian nickname")
        await ctx.send(embed = embed)
        def pred(m):
                    return m.author == ctx.message.author and m.channel == ctx.message.channel
        pseudo_ig = await self.bot.wait_for('message', check=pred)
        pseudo_ig = pseudo_ig.content
        #await ctx.message.delete()
        embed = discord.Embed(description = "Search in Progress...", color = 0xF00000)
        await ctx.send(embed = embed)
        sign_in = await sign_manual(self, entire_pseudo_bot, pseudo_discord, pseudo_ig, ctx)

    @commands.command(pass_context = True, hidden=True)
    async def mm(self, ctx,*args):
        """Mass message for [x|y]
        Def msg: $mm
        for the type : Def, push or Other
        And follow the discussion with the bot"""
        auteur = ctx.message.author
        prefix = ctx.message.author.name
        channel = ctx.guild.get_channel(message_alliance_ig)#message-alliance-ig
        channel_bot = ctx.guild.get_channel(test_bot)
        #Type of message

        #embed = ig et embed_discord = discord
        name_bot = "Super-Fricen"
        embed = discord.Embed(title="%s"%(prefix), color=0xF00000)
        embed_discord = discord.Embed(title="%s"%(prefix), color=0xF00000)
        embed_bot_type = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_x = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_y = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_time = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_msg = discord.Embed(title="%s"%(name_bot), color=0xF00000)


        embed_discord.set_author(name = prefix)
        embed_discord.set_footer(text="Thank you")

        embed.set_author(name = prefix)
        embed.set_footer(text="Thank you")

        embed_bot_type.set_author(name = name_bot)
        embed_bot_type.set_footer(text = "Thank you")

        embed_bot_x.set_author(name = name_bot)
        embed_bot_x.set_footer(text = "Thank you")

        embed_bot_y.set_author(name = name_bot)
        embed_bot_y.set_footer(text = "Thank you")

        embed_bot_time.set_author(name = name_bot)
        embed_bot_time.set_footer(text = "Thank you")

        embed_bot_msg.set_author(name = name_bot)
        embed_bot_msg.set_footer(text = "Thank you")



        embed_bot_type.add_field(name = "Asking Def, Push or Other ? ",value =name_bot)
        await ctx.send(embed = embed_bot_type)

        def pred(m):
                    return m.author == ctx.message.author and m.channel == ctx.message.channel

        type = await self.bot.wait_for('message', check = pred)
        type = type.content

        if(type == 'Other'):
            embed_bot_msg.add_field(name = "Write your message ",value =prefix)
            embed_bot_msg.set_footer(text = "Message : ")
            await ctx.send(embed = embed_bot_msg)
            msg = await self.bot.wait_for('message', check = pred)
            msg = msg.content
            embed.add_field(name ="Information", value = msg)
            await channel.send(embed = embed)
            embed_discord.add_field(name ="Information", value = msg)
            await channel_bot.send(embed = embed_discord)


        else :
            embed_bot_x.add_field(name = "x coord ",value =prefix)
            embed_bot_x.set_footer(text = "Give me x coord : ")
            await ctx.send(embed = embed_bot_x)
            x = await self.bot.wait_for('message', check = pred)
            x = x.content

            embed_bot_y.add_field(name = "y coord ",value =prefix)
            embed_bot_y.set_footer(text = "Give me y coord :")
            await ctx.send(embed = embed_bot_y)
            y = await self.bot.wait_for('message', check = pred)
            y = y.content

            embed_bot_time.add_field(name = "Time ",value =prefix)
            embed_bot_time.set_footer(text = "Give me the time :")
            await ctx.send(embed = embed_bot_time)
            time = await self.bot.wait_for('message', check = pred)
            time = time.content

            if(type=='Def') :
                embed_bot_msg.add_field(name = "How many def needed ? ",value =prefix)
                embed_bot_msg.set_footer(text = "Give me the number total of def needed :")
                await ctx.send(embed = embed_bot_msg)
                msg = await self.bot.wait_for('message', check = pred)
                msg = msg.content
            elif(type == 'Push'):
                embed_bot_msg.add_field(name = "How many ressources by player ? ",value =prefix)
                embed_bot_msg.set_footer(text = "Give me the quantity :")
                await ctx.send(embed = embed_bot_msg)
                msg = await self.bot.wait_for('message', check = pred)
                msg = msg.content

            result = "Hello warriors and amazons,\n\nNeed "+type+" in [x|y]"+x+"|"+y+"[/x|y] for "+time+", server time\nTroops needed : "+msg+"\n\nThank in advance,\n"+prefix
            embed.add_field(name ="Information", value = result)
            await channel.send(embed = embed)
            village = "https://group.europe.travian.com/position_details.php?x=%i&y=%i" %(int(x),int(y))
            embed_discord.set_footer(text="Thank you")
            embed_discord.add_field(name="Village", value = village)
            embed_discord.add_field(name="Time set",value = time)
            embed_discord.add_field(name="Quantity needed", value = msg)
            await channel_bot.send(embed = embed_discord)

    @commands.command(pass_context = True)
    async def info(self, ctx ,*args):
        """Info player
        Use it like $info <Travian nickname>
        """
        auteur = ctx.message.author
        prefix = ctx.message.author.name
        msg = ' '.join(args)
        wb = xlrd.open_workbook('data/Map_Complet.xls')
        sh = wb.sheet_by_name(u'Map_Complet')
        colonne1_id = sh.col_values(1)
        colonne1 = sh.col_values(2)
        colonne2_id = sh.col_values(3)
        colonne2 = sh.col_values(4)
        for rownum in range (sh.nrows):

            if(colonne1[rownum]==msg):
                embed = discord.Embed(title="Information", color=0xff8c00)
                joueur = "https://group.europe.travian.com/spieler.php?uid=%d" %(int(colonne1_id[rownum]))
                alliance = "https://group.europe.travian.com/allianz.php?aid=%d" %(int(colonne2_id[rownum]))
                getter_joueur = "https://www.gettertools.com/group.europe.travian.com/20-Trooptool?getInfo=1&uid=%d" %(int(colonne1_id[rownum]))
                getter_alliance = "https://www.gettertools.com/group.europe.travian.com/20-Trooptool?getInfo=1&aid=%d" %(int(colonne2_id[rownum]))
                embed.add_field(name =msg,value =joueur)
                embed.add_field(name = colonne2[rownum], value = alliance)
                embed.add_field(name ="Getter Player",value =getter_joueur)
                embed.add_field(name = "Getter Alliance", value = getter_alliance)
                await ctx.send(embed=embed)
                return
        await ctx.send("Player doesn't exist")

    @commands.command()
    async def link(self, ctx):
        """Some usefull links"""
        embed = discord.Embed(title="Link", color=0xff8c00)
        embed.add_field(name ="Server",value ="https://group.europe.travian.com")
        embed.add_field(name ="Getter",value ="https://www.gettertools.com/group.europe.travian.com/")
        #embed.add_field(name ="TW WW",value ="http://www.travianwonder.com/uollasww")
        embed.add_field(name ="Kirilloid",value ="http://travian.kirilloid.ru/")
        embed.add_field(name = "Gdoc def", value ="https://docs.google.com/spreadsheets/d/1DEgTNDbJmdO4rV5HYM2hDAShiCYlcZk_8C-VaLLGEJg/edit?ts=5ee0b9b5#gid=440791252")
        await ctx.send(embed=embed)


def setup(bot):
        bot.add_cog(travian(bot))
