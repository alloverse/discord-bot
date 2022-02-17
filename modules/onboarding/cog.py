from ctypes import util
from pydoc import describe
import nextcord, utils
from nextcord.ext import commands
from setuptools import setup
from .onboarding_flow import IntroductionStep

import config

class Onboarding(commands.Cog):
    """Provides new users with an onboarding flow"""
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        # Find welcome channel and update the welcome message
        guild = await self.bot.fetch_guild(config.GUILD_ALLOVERSE)
        await utils.log(guild, "I am ready.")
        channel = guild and await guild.fetch_channel(config.CHANNEL_WELCOME)
        introduction = IntroductionStep()
        try:
            message = await channel.fetch_message(config.MESSAGE_WELCOME)
            await utils.log(guild, "Updating welcome message")
            await message.edit(introduction.message(), view=introduction)
        except nextcord.errors.NotFound:
            await utils.log(guild, "Creating new welcome message")
            await channel.send(introduction.message(), view=introduction)

def setup(bot: commands.Bot):
    bot.add_cog(Onboarding(bot))