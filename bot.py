import os
from nextcord import Intents
from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands

import config

load_dotenv()

bot = commands.Bot(command_prefix='?', intents=Intents(members=True, guilds=True))

bot.load_extension('modules.onboarding.cog')

@bot.slash_command(description="Hello", guild_ids=config.GUILD_IDS)
async def ping(interaction: nextcord.Interaction, message: str):
    await interaction.send(content="Pong: {message}")


bot.run(os.getenv("DISCORD_TOKEN"))