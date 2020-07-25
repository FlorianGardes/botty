import discord
import asyncio
import random
import time
from datetime import datetime
from discord.ext import commands
from options_fricen import *
from discord.utils import *

class serveur(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Supprime le message pour ne laisser que la commande
    '''@command.command(pass_context = True, hidden=True)
    @commands.check(is_owner)
    async def delcmd(ctx, *args):
    msg = ' '.join(args)
        await self.bot.delete_message(ctx.message)
        await self.bot.say(msg) '''
        
    # Message de bienvenue
    async def on_member_join(self, ctx, member):
        channel = get(member.server.channels, name='nouveau-venu')
        await ctx.send_message(channel,'{0.name} à rejoins le server !'.format(member))
        embed=discord.Embed(title="Welcome", color=0x7f07b0)
        embed.add_field(name="G&V server", value = "First, go on #sign-in and type `!sign <pseudo>` with your IG pseudos\nGo in #command for more details on the commands available")
        await ctx.send_message(member, embed=embed)
        #await self.bot.send_message(member,'Bienvenue sur le serveur !\n!help pour avoir les commandes disponibles'.format(member))

    @commands.command(pass_context=True, aliases=['servinfo', 'infoserv', 'infoserver'])
    async def serverinfo(self, ctx):
        """Give some information about this server discord"""
        server = ctx.message.guild
        online = len([m.status for m in server.members
                        if m.status == discord.Status.online or
                        m.status == discord.Status.idle])
        total_users = len(server.members)
        salons_textuels = len([x for x in server.channels
                                if x.type == discord.ChannelType.text])
        salons_vocaux = len(server.channels) - salons_textuels
        jours = (ctx.message.created_at - server.created_at).days
        creation = ("Since {}. That's over {} days ago !""".format(server.created_at.strftime("%d %b %Y"), jours))

        data = discord.Embed(description=creation, colour=discord.Colour(value=0x206694))
        data.add_field(name="Region", value=str(server.region))
        data.add_field(name="Users Online", value="{}/{}".format(online, total_users))
        data.add_field(name="Text Channels", value=salons_textuels)
        data.add_field(name="Voice Channels", value=salons_vocaux)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Owner", value=str(server.owner))
        data.set_footer(text="Server ID: " + str(server.id))

        if server.icon_url:
            data.set_author(name=server.name, url=server.icon_url)
            data.set_thumbnail(url=server.icon_url)
        else:
            data.set_author(name=server.name)

        await ctx.send(embed=data)

    @commands.command(pass_context=True, aliases=['inv'], hidden = True)
    async def invite(self, ctx):
        """Sent an invitation in pm of the server"""
        channel = discord.Object(id=channel_bienvenue)
        auteur = ctx.message.author
        server = ctx.message.guild
        link = await ctx.channel.create_invite(temporary = False, max_uses = 0)
        embedmp = discord.Embed(color=0xf41af4)
        embedmp.add_field(name="Discord invitation link:", value=link)
        embedmp.set_footer(text="%s invited link"%server)
        embed = discord.Embed(description ="Invitation sent in Private Message to **%s**"%auteur, color=0xf41af4)
        await ctx.message.delete()
        await ctx.send(ctx.message.channel, embed=embed)
        await ctx.author.send(auteur, embed=embedmp)


    @commands.command(pass_context = True, hidden=True)
    async def createrole(self, ctx, *args):
        """Créé un role"""
        role = [roles.name.lower() for roles in ctx.message.guild.roles]
        if 'admin' not in role:
            return await ctx.send("**Sorry you are not allowed to make this order!**")
        msg = ' '.join(args)
        auteur = ctx.message.author
        color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        role = await ctx.guild.create_role(name=msg, colour=discord.Colour(color))
        await ctx.send('Role créé avec succes par %s'%auteur )



    @commands.command(pass_context = True, hidden=True)
    async def kick(self, ctx, *, member : discord.Member = None):
        """Kick un membre du serveur"""
        role = [roles.name.lower() for roles in ctx.message.author.roles]

        if 'admin' not in role:
            return await ctx.send("**Sorry you are not allowed to make this order!**")
        if not member:
            return await ctx.send(ctx.message.author.mention + ", please specify the member to kick")
        embed = discord.Embed(description = "**%s** à été kick"%member.name, color = 0xF00000)
        embed.set_footer(text="Bye bye")
        await ctx.guild.kick(member)
        await ctx.send(embed = embed)

    @commands.command(pass_context = True, hidden=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, lignes):
        msg = []
        lignes = int(lignes)
        async for x in ctx.channel.history(limit = lignes):
            msg.append(x)
        deleted = await ctx.message.channel.delete_messages(msg)
        embed = discord.Embed(description = "**%s** message deleted by **%s**"%(lignes, ctx.message.author), color = 0xF00000)
        embed.set_footer(text="Clear")
        await ctx.send(embed = embed)

def setup(bot):
        bot.add_cog(serveur(bot))
