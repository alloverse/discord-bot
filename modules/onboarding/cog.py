from pydoc import describe
import nextcord
from nextcord.ext import commands
from setuptools import setup
from .onboarding_flow import IntroductionStep

from bot import GUILD_IDS

class Onboarding(commands.Cog):
    """Provides new users with an onboarding flow"""
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        #Find welcomechannel and fix the welcome message
        welcome_channel = 941699504141377536
        channel = None
        introduction = IntroductionStep()
        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.id == welcome_channel:
                    try:
                        message = await channel.fetch_message(943554424465403934)
                        await message.edit(introduction.message(), view=introduction)
                    except:
                        await channel.send(introduction.message(), view=introduction)
        

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        channel = member.guild.system_channel or member.guild.get_channel(941699504141377536)
        print("A member joined", member, str(member), member.guild.system_channel, member.guild.id)

        if (str(member) == "Voxar#6375" or str(member) == "Tobi#4874") and member.guild.id == 938806794111819816:
            role = member.guild.get_role(942714069037748234)
            if role:
                await member.send("Hello creator. I gave you admin powers 🧙‍♀️")
                await member.add_roles(role)
            else:
                print("Failed to fetch the wizard role")
        

    @nextcord.slash_command(guild_ids=GUILD_IDS)
    async def onboarding(self, interaction: nextcord.Interaction):
        """Begins the onboarding flow"""
        introduction = IntroductionStep()
        await interaction.send(introduction.message(), view=introduction, ephemeral=True)
    

def setup(bot: commands.Bot):
    bot.add_cog(Onboarding(bot))