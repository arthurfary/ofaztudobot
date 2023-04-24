import discord
from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Argumento obrigatório faltando. ({error.param.name})")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Este comando não existe. ({ctx.command.name})")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Você não tem permissão para usar este comando. ({error.missng_perms[0]})") 
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Membro não encontrado.")
        else:
            await ctx.send(f"Um erro ocorreu: {error}.")