import os
import discord
from discord.ext import commands

from cogs.greetings_cog import Greetings



# Get the Discord token from the environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Add the Greetings cog to the bot within an async function
@bot.event
async def on_ready():

    print('> Loading cogs...')

    await bot.add_cog(Greetings(bot))

    print('> Cogs loaded!')

    print('> Running!')

# Run the bot with your bot token from the .env file
bot.run(TOKEN)