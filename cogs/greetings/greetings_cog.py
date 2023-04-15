import discord
from discord.ext import commands

class Greetings(commands.Cog):
    '''
    Classe com mensagens de boas vindas!
    '''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ola(self, ctx):
        await ctx.send(f'Olá {ctx.message.author.name}!')


    # mais commandos de oi
