# main.py
import os
import discord
import platform
import datetime
import logging
import asyncio
from discord.ext import commands
from src import helpers, checks, db



# Start up the discord logging module.
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
error_handler = logging.FileHandler(filename='discord_errors.log', encoding='utf-8', mode='w')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(error_handler)
logger.addHandler(handler)




# load all the enviromental variables 
config_vars = helpers.fetch_config()

token = config_vars["token"]
owner = config_vars["owner"]
default_prefix = config_vars["prefix"]
allowed_server = config_vars["allowed_server"]
management_role = config_vars["management_role"]
bypassed_users = config_vars["bypassed_users"]

# Creating the bot class
bot = commands.Bot(command_prefix = default_prefix, case_insensitive = True)

# Removing the default help command
bot.remove_command('help')

# Defining the on_ready event
@bot.event
async def on_ready():
    # Print the bot invite link
    print(f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=519232&scope=bot")
    print(f"Logged on as {bot.user}!")
    
    await bot.change_presence(
        activity = discord.Game(name="Watching our important messages!")
    )   # Change the presence of the bot
    uri = helpers.fetch_config('postgres')
    await db.start_pool(uri)
    

@bot.event
async def on_guild_join(guild):
    channel = guild.system_channel
    embed = helpers.create_embed(
        "Hi there!",
        16761035,
        [
            ["Startup!", "Thank you for inviting me to your server! \nMy prefix here is: `{prefix}`\nHead over to the (README)[https://github.com/AnotherCat/custom_helper_bot/blob/master/README.md] for setup instructions!"]
        ]
    )
    channel.send(embed=embed)

"""@bot.event
async def on_error(ctx, error):
    logger.error(error)"""

@bot.event
async def on_message(message):
    prefix = await db.return_pool().get_prefix(message.guild.id)
    if not prefix:
        await bot.process_commands(message)
    elif message.content.startswith(prefix):
        message.content = f'{default_prefix}{message.content[len(prefix):]}'
        await bot.process_commands(message)
    

extensions = [
    'cogs.maincog',
    'cogs.messages',
    'cogs.admin',
    'cogs.stats'
]
for extension in extensions:
    bot.load_extension(extension)
    
bot.run(token)
