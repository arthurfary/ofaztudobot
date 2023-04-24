import discord
from discord.ext import commands
import random
from discord.ext.commands.converter import MemberConverter
import datetime

class Management(commands.Cog):
    '''
    Classe com comandos de gerenciamentos
    '''

    def __init__(self, bot):
        self.bot = bot
       

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def castigo(self, ctx, member: MemberConverter, time: int = 15, *, reason = 'Por que sim!'):
        
        await member.timeout(datetime.timedelta(seconds=time), reason = reason)
        await ctx.send(f'Castigo dado a {member.name}: {reason}')
            
            


    # mais commandos de oi
