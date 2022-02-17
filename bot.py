import os
from nextcord import Intents
from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands

import config

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=Intents(members=True, guilds=True))

bot.load_extension('modules.onboarding.cog')

bot.run(os.getenv("DISCORD_TOKEN"))