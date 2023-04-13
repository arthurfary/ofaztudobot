import os
import discord
from discord.ext import commands

from cogs.greetings_cog import Greetings
from cogs.fun_cog import Fun

# Get the Discord token from the environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Add the Greetings cog to the bot within an async function
@bot.event
async def on_ready():
    print('> Loading cogs...')

    # bot cogs

    await bot.add_cog(Greetings(bot))
    await bot.add_cog(Fun(bot))

    print('> Cogs loaded!')
    print('> Bot ready!')

    

# Run the bot with your bot token from the .env file
if __name__ == '__main__':
    
    bot.run(TOKEN)
    