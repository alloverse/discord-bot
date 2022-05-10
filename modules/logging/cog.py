from ctypes import util
from pydoc import describe
from sre_constants import LITERAL_LOC_IGNORE
import nextcord, utils
from nextcord.ext import commands
from setuptools import setup
from . import logserver
import asyncio

import config

class LogHandler(logserver.Handler):
    async def on_event_async(self, js): 
        print("cog?", self.cog)
        bot = self.cog.bot
        guild = await bot.fetch_guild(config.GUILD_ALLOVERSE)
        await utils.log(guild, "I am ready.")
        channel = guild and await guild.fetch_channel(config.CHANNEL_APPLICATION_LOGS)
        await channel.send("event: {event_name}, data: {event_data}".format(**js))

    def on_event(self, js):
        super().on_event(js)
        asyncio.run_coroutine_threadsafe(self.on_event_async(js), self.runloop)


def make_handler(request, address, server):
    return LogHandler(request=request, client_address=address, server=server)

class AlloverseLogReporting(commands.Cog):
    """Provides new users with an onboarding flow"""
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        # Find welcome channel and update the welcome message
        LogHandler.cog = self
        LogHandler.runloop = self.bot.loop
        logserver.run_logging_server(LogHandler)
        
        print("Log handler started")

def setup(bot: commands.Bot):
    bot.add_cog(AlloverseLogReporting(bot))