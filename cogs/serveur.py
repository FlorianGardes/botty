import discord
import asyncio
import random
from discord.ext import commands
from options_fricen import *
from discord.utils import *

def is_allow(ctx):
    for allowed in Allow_Id:
        if ctx.message.author.id == allowed:
            return True
    return False

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
    
    # Permet de vérifier le bon lancement du bot
    async def on_ready(self):
        print('--------------------------------')
        print('Bot connecté')
        print('Username : {}'.format(self.bot.user.name))
        print('ID : {}'.format(self.bot.user.id))
        print('discord.py v{}'.format(discord.__version__))
        print('Nombre de serveur infectés:', str(len(self.bot.servers)))
        print('Nombre de personnes visibles:',len(set(self.bot.get_all_members())))
        print('--------------------------------')
        #await self.bot.change_presence(game=(discord.Game(name='{}help'.format(CommandPrefix))))
        
    # Message de bienvenue
    async def on_member_join(self, member):
        channel = get(member.server.channels, name='nouveau-venu')
        await self.bot.send_message(channel,'{0.name} à rejoins le server !'.format(member))
        embed=discord.Embed(title="Welcome", color=0x7f07b0)
        embed.add_field(name="G&V server", value = "First, go on #sign-in and type `!sign <pseudo>` with your IG pseudos\nGo in #command for more details on the commands available")
        await self.bot.send_message(member, embed=embed)
        #await self.bot.send_message(member,'Bienvenue sur le serveur !\n!help pour avoir les commandes disponibles'.format(member))

    @commands.command(pass_context=True, aliases=['servinfo', 'infoserv', 'infoserver'])
    async def serverinfo(self, ctx):
        """Give some information about this server discord"""
        server = ctx.message.server
        online = len([m.status for m in server.members
                        if m.status == discord.Status.online or
                        m.status == discord.Status.idle])
        total_users = len(server.members)
        salons_textuels = len([x for x in server.channels
                                if x.type == discord.ChannelType.text])
        salons_vocaux = len(server.channels) - salons_textuels
        jours = (ctx.message.timestamp - server.created_at).days
        creation = ("Since {}. That's over {} days ago !""".format(server.created_at.strftime("%d %b %Y"), jours))

        data = discord.Embed(description=creation, colour=discord.Colour(value=0x206694))
        data.add_field(name="Region", value=str(server.region))
        data.add_field(name="Users Online", value="{}/{}".format(online, total_users))
        data.add_field(name="Text Channels", value=salons_textuels)
        data.add_field(name="Voice Channels", value=salons_vocaux)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Owner", value=str(server.owner))
        data.set_footer(text="Server ID: " + server.id)

        if server.icon_url:
            data.set_author(name=server.name, url=server.icon_url)
            data.set_thumbnail(url=server.icon_url)
        else:
            data.set_author(name=server.name)

        await self.bot.say(embed=data)

    @commands.command(pass_context=True, aliases=['inv'], hidden = True)
    async def invite(self, ctx):
        """Sent an invitation in pm of the server"""
        channel = discord.Object(id=channel_bienvenue)
        auteur = ctx.message.author
        server = ctx.message.server
        link = await self.bot.create_invite(destination = channel, temporary = False, max_uses = 0)
        embedmp = discord.Embed(color=0xf41af4)
        embedmp.add_field(name="Discord invitation link:", value=link)
        embedmp.set_footer(text="%s invited link"%server)
        embed = discord.Embed(description ="Invitation sent in Private Message to **%s**"%auteur, color=0xf41af4)
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, embed=embed)
        await self.bot.send_message(auteur, embed=embedmp)


    @commands.command(pass_context = True, hidden = True, brief= "Add role to author")
    async def addrole(ctx,*args):
        msg = ' '.join(args)
        auteur = ctx.message.author
        role_serveur = [roles.name.lower() for roles in ctx.message.server.roles]
        role_member = [roles.name.lower() for roles in ctx.message.author.roles]
        if (msg not in role_serveur):
            if(msg not in role_member):
                role = await self.bot.create_role(auteur.server, name=msg)
                await selfbot.say('%s has been added by %s'%(msg,auteur) )
            await self.bot.say("You have already this role")
        await self.bot.say("Role has not been created")


    @commands.command(pass_context = True, hidden=True)
    async def createrole(self, ctx, *args):
        """Créé un role"""
        role = [roles.name.lower() for roles in ctx.message.server.roles]
        if 'admin' not in role:
            return await self.bot.say("**Sorry you are not allowed to make this order!**")
        msg = ' '.join(args)
        auteur = ctx.message.author
        color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        role = await self.bot.create_role(auteur.server, name=msg, colour=discord.Colour(color))
        await self.bot.say('Role créé avec succes par %s'%auteur )



    @commands.command(pass_context = True, hidden=True)
    async def kick(self, ctx, *, member : discord.Member = None):
        """Kick un membre du serveur"""
        role = [roles.name.lower() for roles in ctx.message.author.roles]

        if 'admin' not in role:
            return await self.bot.say("**Sorry you are not allowed to make this order!**")
        if not member:
            return await self.bot.say(ctx.message.author.mention + ", please specify the member to kick")
        embed = discord.Embed(description = "**%s** à été kick"%member.name, color = 0xF00000)
        embed.set_footer(text="Bye bye")
        await self.bot.kick(member)
        await self.bot.say(embed = embed)

    @commands.command(pass_context = True, hidden=True)
    @commands.check(is_allow)
    async def clear(self, ctx, lignes):
        mgs = []
        lignes = int(lignes)
        async for x in self.bot.logs_from(ctx.message.channel, limit = lignes+1):
            mgs.append(x)
        await self.bot.delete_messages(mgs)
        embed = discord.Embed(description = "**%s** message deleted by **%s**"%(lignes, ctx.message.author), color = 0xF00000)
        embed.set_footer(text="Clear")
        await self.bot.say(embed = embed)

def setup(bot):
    bot.add_cog(serveur(bot))
