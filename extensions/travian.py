import discord
import asyncio
import xlrd
import xlwt
import random
import datetime
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
        channel_bot = ctx.guild.get_channel(hc_using_bot)
        channel_def = ctx.guild.get_channel(message_def)
        channe_other = ctx.guild.get_channel(message_alliance)
        #Type of message

        #embed = ig et embed_discord = discord
        name_bot = "Super-Fricen"
        embed = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_discord = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_type = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_x = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_y = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_time = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_msg = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_type.add_field(name = "Asking def, push or something else ? ",value ="Write exactly Def, Push or Other")
        await ctx.send(embed = embed_bot_type)

        def pred(m):
                    return m.author == ctx.message.author and m.channel == ctx.message.channel

        type = await self.bot.wait_for('message', check = pred)
        type = type.content

        if(type == 'Other'):
            embed_bot_msg.add_field(name = "What is you message you want to transmit ",value ="Write your message ")
            await ctx.send(embed = embed_bot_msg)
            msg = await self.bot.wait_for('message', check = pred)
            msg = msg.content
            embed.add_field(name ="Information", value = msg)
            await channel.send(embed = embed)



        else :
            embed_bot_x.add_field(name = "x coord ",value ="20 for example")
            embed_bot_x.set_footer(text = "Give me x coord : ")
            await ctx.send(embed = embed_bot_x)
            x = await self.bot.wait_for('message', check = pred)
            x = x.content

            embed_bot_y.add_field(name = "y coord ",value ="20 for example")
            embed_bot_y.set_footer(text = "Give me y coord :")
            await ctx.send(embed = embed_bot_y)
            y = await self.bot.wait_for('message', check = pred)
            y = y.content

            embed_bot_time.add_field(name = "Time ",value ="For example 17h or 17:00:00")
            embed_bot_time.set_footer(text = "Give me the time :")
            await ctx.send(embed = embed_bot_time)
            time = await self.bot.wait_for('message', check = pred)
            time = time.content

            if(type=='Def') :
                embed_bot_msg.add_field(name = "How many def needed ? ",value ="For example 50k or 50000 or 50 000")
                embed_bot_msg.set_footer(text = "Give me the number total of def needed :")
                await ctx.send(embed = embed_bot_msg)
                msg = await self.bot.wait_for('message', check = pred)
                msg = msg.content

                result = "Hello warriors and amazons,\n\nNeed "+type+" in [x|y]"+x+"|"+y+"[/x|y] for "+time+", server time\nTroops needed : "+msg+"\n\nThank in advance,\n"+prefix
                embed.add_field(name ="Information", value = result)
                await channel.send(embed = embed)
                village = serveur_travian + "/position_details.php?x="+str(int(x))+"&y=" +str(int(y))
                embed_discord.set_footer(text="Thank you")
                embed_discord.add_field(name="Village", value = village)
                embed_discord.add_field(name="Time set",value = time)
                embed_discord.add_field(name="Quantity needed", value = msg)
                await channel_def.send(embed = embed_discord)
            elif(type == 'Push'):
                embed_bot_msg.add_field(name = "How many ressources by player ? ",value ="For example 2k or 2000 or 2 000")
                embed_bot_msg.set_footer(text = "Give me the quantity :")
                await ctx.send(embed = embed_bot_msg)
                msg = await self.bot.wait_for('message', check = pred)
                msg = msg.content

                result = "Hello warriors and amazons,\n\nNeed "+type+" in [x|y]"+x+"|"+y+"[/x|y] for "+time+", server time\nTroops needed : "+msg+"\n\nThank in advance,\n"+prefix
                embed.add_field(name ="Information", value = result)
                await channel.send(embed = embed)
                village = serveur_travian + "/position_details.php?x="+str(int(x))+"&y=" +str(int(y))
                embed_discord.set_footer(text="Thank you")
                embed_discord.add_field(name="Village", value = village)
                embed_discord.add_field(name="Time set",value = time)
                embed_discord.add_field(name="Quantity needed", value = msg)
                await channe_other.send(embed = embed_discord)

            

    @commands.command(pass_context = True, hidden=True)
    async def reports_add(self, ctx,*args):
        name_bot = "Super-Fricen"
        #Embed du bot
        embed_bot_name = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_x = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_y = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_report = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_fin = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_date = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        #Map_Complet
        Doc_data_name = xlrd.open_workbook('data/Map_Complet.xls')
        sheet_data_name = Doc_data_name.sheet_by_name(u'Map_Complet')
        pseudo = sheet_data_name.col_values(2)
        pseudo_trouve = False
        #Reports_read
        Doc_report_read = xlrd.open_workbook('data/Reports.xls')
        sheet_report = Doc_report_read.sheet_by_name(u'Model')
        player = sheet_report.col_values(0)
        #reports_write
        Doc_report_write = xlwt.Workbook()
        sheet_report_write = Doc_report_write.add_sheet(u'Model')

        await ctx.message.delete()
        embed_bot_name.add_field(name = "Name of ennemy ? ",value ="Exact name IG")
        await ctx.send(embed = embed_bot_name)
        

        def pred(m):
                    return m.author == ctx.message.author and m.channel == ctx.message.channel

        name = await self.bot.wait_for('message', check = pred)
        name = name.content
        
        for rownum in range(sheet_data_name.nrows):
            if(pseudo[rownum]==name):
                pseudo_trouve = True

        if(pseudo_trouve == True) :
            embed_bot_x.add_field(name = "X ",value ="50 for example")
            await ctx.send(embed = embed_bot_x)
            coord_x = await self.bot.wait_for('message', check = pred)
            coord_x = coord_x.content

            embed_bot_y.add_field(name = "Y ",value ="50 for example")
            await ctx.send(embed = embed_bot_y)
            coord_y = await self.bot.wait_for('message', check = pred)
            coord_y = coord_y.content

            embed_bot_report.add_field(name = "Link of report ",value ="link shared on internet, like traviantools or lightshot")
            await ctx.send(embed = embed_bot_report)
            link_report = await self.bot.wait_for('message', check = pred)
            link_report = link_report.content
            
            embed_bot_date.add_field(name = "Date ",value ="29/10 for example")
            await ctx.send(embed = embed_bot_date)
            date = await self.bot.wait_for('message', check = pred)
            date = date.content

            i = 0
            for ligne_free in range(sheet_report.nrows) :
                if(player[ligne_free] == '') :
                    break
                sheet_report_write.write(ligne_free, 0, sheet_report.cell_value(ligne_free,0))
                sheet_report_write.write(ligne_free, 1, sheet_report.cell_value(ligne_free,1))
                sheet_report_write.write(ligne_free, 2, sheet_report.cell_value(ligne_free,2))
                sheet_report_write.write(ligne_free, 3, sheet_report.cell_value(ligne_free,3))
                sheet_report_write.write(ligne_free, 4, sheet_report.cell_value(ligne_free,4))
                i = i+1

            ligne_free = i
            sheet_report_write.write(ligne_free, 0, name)
            sheet_report_write.write(ligne_free, 1, coord_x)
            sheet_report_write.write(ligne_free, 2, coord_y)
            sheet_report_write.write(ligne_free, 3, link_report)
            sheet_report_write.write(ligne_free, 4, date)

            embed_bot_fin.add_field(name = "We are done ",value ="Bye")
            await ctx.send(embed = embed_bot_fin)

            Doc_report_write.save('data/Reports.xls')
        else :
            embed_bot_fin.add_field(name = "Wrong name ", value= "Be sure to put the exact name IG of the player")
            await ctx.send(embed = embed_bot_fin)
        return

    @commands.command(pass_context = True, hidden=True)
    async def reports_read(self, ctx,*args):
        name_bot = "Super-Fricen"
        #Embed du bot
        embed_bot_name = discord.Embed(title="%s"%(name_bot), color=0xF00000)
        embed_bot_fin = discord.Embed(title="%s"%(name_bot), color=0xF00000)

        embed_bot_name.set_footer(text = "Thank you")
        #Map_Complet
        Doc_data_name = xlrd.open_workbook('data/Map_Complet.xls')
        sheet_data_name = Doc_data_name.sheet_by_name(u'Map_Complet')
        pseudo = sheet_data_name.col_values(2)
        pseudo_trouve = False
        #Reports_read
        Doc_report_read = xlrd.open_workbook('data/Reports.xls')
        sheet_report = Doc_report_read.sheet_by_name(u'Model')
        player = sheet_report.col_values(0)
        x = sheet_report.col_values(1)
        y = sheet_report.col_values(2)
        link = sheet_report.col_values(3)
        date = sheet_report.col_values(4)

        await ctx.message.delete()

        embed_bot_name.add_field(name = "Name of ennemy ? ",value ="Give me the exact pseudo")
        await ctx.send(embed = embed_bot_name)

        def pred(m):
                    return m.author == ctx.message.author and m.channel == ctx.message.channel

        name = await self.bot.wait_for('message', check = pred)
        name = name.content 


        for rownum in range(sheet_data_name.nrows):
            if(pseudo[rownum]==name):
                pseudo_trouve = True
        if(pseudo_trouve == True) :
            for player_sheet in range(sheet_report.nrows) :
                if(player[player_sheet]==name) :
                    embed_bot_fin.add_field(name = date[player_sheet],value =str(x[player_sheet]) +"/" + str(y[player_sheet]) + " report : " + link[player_sheet])
            embed_bot_fin.set_author(name = name )
            await ctx.send(embed = embed_bot_fin)
        else :
            embed_bot_fin.add_field(name = "Wrong name ", value= "Be sure to put the exact name IG of the player")
            await ctx.send(embed = embed_bot_fin)
        return

    @commands.command(pass_context = True)
    async def info(self, ctx ,*args):
        """Info player
        Use it like $info <Travian nickname>
        """
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
                joueur = serveur_travian+"/spieler.php?uid=" +str(int(colonne1_id[rownum]))
                alliance = serveur_travian+"/allianz.php?aid=" +str(int(colonne2_id[rownum]))
                getter_joueur = getter+"/20-Trooptool?getInfo=1&uid=" +str(int(colonne1_id[rownum]))
                getter_alliance = getter+"/20-Trooptool?getInfo=1&aid=" +str(int(colonne2_id[rownum]))
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
        embed.add_field(name ="Server",value =serveur_travian)
        embed.add_field(name ="Getter",value =getter)
        #embed.add_field(name ="TW WW",value ="http://www.travianwonder.com/uollasww")
        embed.add_field(name ="Kirilloid",value =kiri)
        embed.add_field(name = "Gdoc def", value =gdoc_def)
        await ctx.send(embed=embed)


def setup(bot):
        bot.add_cog(travian(bot))
