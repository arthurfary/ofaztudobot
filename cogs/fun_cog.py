import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    '''
    Classe com mensagens de boas vindas!
    '''

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def penis(self, ctx):
        '''
        Mostra o tamnho (real) do pipi da pessoa
        '''
        ppsize = 15
        penis = '8'
        
        for i in range(random.randrange(ppsize)):
            penis += '='

        penis += 'D' 

        await ctx.send(f'Seu pipi é desse tamanho: {penis}')


    @commands.command()
    async def tapa(self, ctx, 
                    name: str = commands.parameter(description="Nome de quem será tapeado"), 
                    *, reason: str = commands.parameter(default="motivo nenhum", description="Motivo do tapeamento")):
        '''
        Estapeia alguém!

        Usage:
            !tapa <name> <reason>

        Example:
            !tapa nome reason
            !tapa @yut#7995 ser muito bacana

        '''
        await ctx.send(f'{ctx.message.author.name} deu um tapa em {name} por {reason} :clap:')


    # mais commandos de oi
