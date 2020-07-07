import discord
import asyncio
import xlrd
import random
from discord.ext import commands
from options_fricen import *
from discord.utils import *

def is_channel(channel_id):
    def predicate(ctx):
        return ctx.message.channel.id == channel_id
    return commands.check(predicate)

class travian:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    #@is_channel(channel_inscription)
    async def sign(self, ctx, *args):
        """Allows to register
        Use it with your own pseudo IG like !sign <pseudo>
        """
        auteur = ctx.message.author
        prefix = ctx.message.author.name
        msg = ' '.join(args)
        wb = xlrd.open_workbook('data/Map_Complet.xls')
        sh = wb.sheet_by_name(u'Map_Complet')
        colonne1 = sh.col_values(2)
        colonne2 = sh.col_values(4)
        colonne3 = sh.col_values(0)
        for rownum in range(sh.nrows):
                if(colonne1[rownum]==msg):
                    role_name = colonne2[rownum]
                    pseudo = colonne1[rownum]
                    role = [roles.name.lower() for roles in ctx.message.server.roles]
                    if (role_name.lower()) not in role:
                        color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                        color = int(color, 16)
                        role = await self.bot.create_role(auteur.server, name=role_name, colour=discord.Colour(color))
                        await self.bot.add_roles(auteur, role)
                        pseudo = prefix + ' (' + pseudo +')'
                        await self.bot.change_nickname(auteur, pseudo)
                        embed = discord.Embed(description = "**%s** has been created and added to **%s**"%(role_name, prefix), color = 0xF00000)
                        await self.bot.say(embed = embed)
                        return
                    role = get(ctx.message.server.roles, name=role_name)
                    await self.bot.add_roles(auteur, role)
                    pseudo = prefix + ' (' + pseudo +')'
                    await self.bot.change_nickname(auteur, pseudo)
                    embed = discord.Embed(description = "**%s** has been assigned and added to **%s**"%(role, prefix), color = 0xF00000)
                    await self.bot.say(embed = embed)
                    return
        await self.bot.say("Player doesn't exist, try again")

    @commands.command(pass_context = True, hidden=True)
    async def mm(self, ctx,*args):
        """Mass message for [x|y]
        Def msg: !mm def x y hour troops food
        Example: !mm def 205 77 17:19:00 all yes
        ======================================
        Push msg: !mm push x y hour quantity
        Example: !mm push 121 122 14:00:00 30"""
        auteur = ctx.message.author
        prefix = ctx.message.author.name
        channel = discord.Object(id=message_alliance_ig)#message-alliance-ig
        channel_test = discord.Object(id=test_bot)#test-bot
        channel_message = discord.Object(id=message_alliance)#message-alliance
        if(args[0] == 'help'):
            msg ="For prepare mm (def, push or feeding), you need args like :\n!mm def x y hour quantit_of_troops feed(yes or np)\n!mm push x y hour(hh:mm:ss) quantity/player\n!mm crops x y"
            embed=discord.Embed(title="Help mass message", color=0x1ea91e)
            embed.add_field(name="Command :" , value=msg)
            embed.set_footer(text="group.europe.travian.com")
            embed.set_author(name=prefix)
            await self.bot.send_message(channel_test,embed=embed)
            return
        elif(args[0] =='def'):
            if(args[5]=='yes'):
                msg ="Hello,\n\nNeed def for [x|y]"+args[1]+"|"+args[2]+"[/x|y] for "+args[3]+" , server time\nQuantity needed : "+args[4]+"k\nDon't forget to feed\n\nThanks in advance,\n"+prefix
                embed=discord.Embed(title="Asking def", color=0x1ea91e)
                embed.set_author(name=prefix)
                embed.set_footer(text="group.europe.travian.com")
                embed.add_field(name="Message : ", value=msg)


                village = "https://group.europe.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
                embed_discord=discord.Embed(title="Asking def wall", color=0x1ea91e)
                embed_discord.set_author(name=prefix)
                embed_discord.set_footer(text="Thank you")
                embed_discord.add_field(name="Village to def", value = village)
                embed_discord.add_field(name="Time set",value = args[3])
                embed_discord.add_field(name="Troops needed ( in k )", value = args[4])
                embed_discord.add_field(name = "Need to feed ?  ", value = "Yes")
                await self.bot.send_message(channel,embed=embed)
                await self.bot.send_message(channel_message,embed=embed_discord)

            else :
                msg = "Hello warriors and amazons,\n\nNeed def in [x|y]"+args[1]+"|"+args[2]+"[/x|y] for "+args[3]+", server time\nTroops needed : "+args[4]+"k\nNo need to feed\n\nThank in advance,\n"+prefix
                embed=discord.Embed(title="Asking def wall", color=0x1ea91e)
                embed.set_author(name=prefix)
                embed.set_footer(text="group.europe.travian.com")
                embed.add_field(name="Message : ", value=msg)



                village = "https://group.europe.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
                embed_discord=discord.Embed(title="Asking Def Wall", color=0x1ea91e)
                embed_discord.set_author(name=prefix)
                embed_discord.set_footer(text="Thank you")
                embed_discord.add_field(name="Village to def", value = village)
                embed_discord.add_field(name="Time set",value = args[3])
                embed_discord.add_field(name="Troops needed ( in k ) ", value = args[4])
                embed_discord.add_field(name = "Need to feed ? ", value = "No")
                await self.bot.send_message(channel,embed=embed)
                await self.bot.send_message(channel_message,embed=embed_discord)
        elif(args[0]=='push'):
            msg = "Hello everyone,\n\nPush in [x|y]"+args[1]+"|"+args[2]+"[/x|y] until "+args[3]+" , server time\n"+args[4]+"k/player asked\n\nThank you in advance,\n"+prefix
            embed=discord.Embed(title="Push", color=0x1ea91e)
            embed.set_author(name=prefix)
            embed.set_footer(text="group.europe.travian.com")
            embed.add_field(name="Message : ", value=msg)

            village = "https://group.europe.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
            embed_discord=discord.Embed(title="Push", color=0x1ea91e)
            embed_discord.set_author(name=prefix)
            embed_discord.set_footer(text="Thank you")
            embed_discord.add_field(name="Village to push", value = village)
            embed_discord.add_field(name="Hour",value = args[3])
            embed_discord.add_field(name="Quantity asked ( in k )", value = args[4])
            await self.bot.send_message(channel,embed=embed)
            await self.bot.send_message(channel_message,embed=embed_discord)

        elif(args[0]=='crops'):
            msg = "Hello everyone,\n\nDon't forget to feed in [x|y]"+args[1]+"|"+args[2]+"[/x|y],\nThank you in advance\n"+prefix
            embed=discord.Embed(title="Crops", color=0x1ea91e)
            embed.set_author(name=prefix)
            embed.set_footer(text="group.europe.travian.com")
            embed.add_field(name="Need crops : ", value=msg)

            village = "https://group.europe.travian.com/position_details.php?x=%i&y=%i" %(int(args[1]),int(args[2]))
            embed_discord=discord.Embed(title="Push", color=0x1ea91e)
            embed_discord.set_author(name=prefix)
            embed_discord.set_footer(text="Thank you")
            embed_discord.add_field(name="Village to feed", value = village)
            await self.bot.send_message(channel,embed=embed)
            await self.bot.send_message(channel_message,embed=embed_discord)

    @commands.command(pass_context = True)
    async def info(self, ctx ,*args):
        """Info player
        Use like !info <pseudo>
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
                embed.add_field(name =msg,value =joueur)
                embed.add_field(name = colonne2[rownum], value = alliance)
                await self.bot.say(embed=embed)
                return
        await self.bot.say("Player doesn't exist")

    @commands.command()
    async def link(self):
        """Some usefull links"""
        embed = discord.Embed(title="Link", color=0xff8c00)
        embed.add_field(name ="Server",value ="https://group.europe.travian.com")
        embed.add_field(name ="Getter",value ="https://www.gettertools.com/group.europe.travian.com/")
        #embed.add_field(name ="TW WW",value ="http://www.travianwonder.com/uollasww")
        embed.add_field(name ="Kirilloid",value ="http://travian.kirilloid.ru/")
        #embed.add_field(name = "Gdoc def", value ="https://docs.google.com/spreadsheets/d/1kYZnD2GsUd2nNRjc4o5fFvvXrqhZ9YnAwguosK5dVCA/edit#gid=440791252")
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(travian(bot))
