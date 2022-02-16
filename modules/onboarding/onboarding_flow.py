import config
from utils import button_id
from discord import Embed
import nextcord
from nextcord.ext import commands


class OnboardingFlow(object):
    def __init__(self, bot: commands.Bot, user: nextcord.User) -> None:
        self.bot = bot
        self.user = user
        self.step = 0

    def next_response(self):
        Embed()

class IntroductionStep(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(label="Build a VR app", emoji="🛠")
    async def build_vr_button(self, button, interaction):
        print(f"Pressed {button.label} button")

    @nextcord.ui.button(label="Help build Alloverse", emoji="🚧")
    async def build_alloverse_button(self, button, interaction):
        print(f"Pressed {button.label} button")

    @nextcord.ui.button(label="File a bug", emoji="🐞")
    async def file_a_bug_button(self, button, interaction):
        print(f"Pressed {button.label} button")
    
    @nextcord.ui.button(label="Just look around", emoji="👀")
    async def just_looking_around_button(self, button, interaction):
        print(f"Pressed {button.label} button")

class BuildVrAppStep(nextcord.ui.View):
    @nextcord.ui.button(label="I'm kind of a newbie", emoji="👾")
    async def beginner(self, button, interaction):
        print(f"Pressed {button.label} button")

    @nextcord.ui.button(label="3D Stuff", emoji="🫖")
    async def three_dee(self, button, interaction):
        print(f"Pressed {button.label} button")

    @nextcord.ui.button(label="2D Stuff", emoji="👩‍🎨")
    async def two_dee(self, button, interaction):
        print(f"Pressed {button.label} button")


class BuildAlloverseAppStep(nextcord.ui.View):
    @nextcord.ui.button(label="Coding", emoji="👩‍💻")
    async def coding(self, button, interaction):
        print(f"Pressed {button.label} button")

    @nextcord.ui.button(label="Design", emoji="👩‍🎨")
    async def design(self, button, interaction):
        print(f"Pressed {button.label} button")

    @nextcord.ui.button(label="Finiancial contributions", emoji="💰")
    async def design(self, button, interaction):
        print(f"Pressed {button.label} button")

    @nextcord.ui.button(label="Discord Boosting", emoji="🔋")
    async def design(self, button, interaction):
        print(f"Pressed {button.label} button")

    @nextcord.ui.button(label="Spreading the word", emoji="📣")
    async def design(self, button, interaction):
        print(f"Pressed {button.label} button")

    @nextcord.ui.button(label="Other", emoji="🌎")
    async def design(self, button, interaction):
        print("Pressed Other button")

