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
        self.bot.add_view(IntroductionStep())

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
        if channel:
            message = f"Welcome {member.mention}, what would you like to do in our server?"
            await channel.send(message, view=IntroductionStep())
        

    @nextcord.slash_command(guild_ids=GUILD_IDS)
    async def onboarding(self, interaction: nextcord.Integration):
        """Begins the onboarding flow"""
        message = f"Welcome {interaction.user.mention}, what would you like to do in our server?"
        await interaction.send(message, view=IntroductionStep())
    

def setup(bot: commands.Bot):
    bot.add_cog(Onboarding(bot))