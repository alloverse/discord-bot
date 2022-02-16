from code import interact
from email import message
from re import S
import config
from utils import button_id
from discord import Embed, Interaction
import nextcord
from nextcord import Interaction, Message, User, Member
from nextcord.ext import commands
from typing import Optional

    
class IntroPage(nextcord.ui.View):
    def __init__(self, prev: nextcord.ui.View = None):
        super().__init__(timeout=None)
        self.prev = prev

    def message(self): 
        return "So..."

class CompletePage(IntroPage):
    def __init__(self, prev: nextcord.ui.View, text):
        super().__init__(prev=prev)
        self.text = text
        self.prev = prev

    def message(self): 
        return self.text

    @nextcord.ui.button(emoji="🔙")
    async def go_back(self, button, interaction: Interaction):
        if self.prev:
            await interaction.edit_original_message(self.prev.message(), view=self.prev)
        else:
            await interaction.delete_original_message()

class IntroductionStep(IntroPage):
    def message(self):
        return f"Welcome, what would you like to do in our server?"

    @nextcord.ui.button(label="Build a VR app", emoji="🛠")
    async def build_vr_button(self, button, interaction: Interaction):
        next = BuildVrAppStep(self)
        await interaction.send(next.message(), view=next, ephemeral=True)

    @nextcord.ui.button(label="Help build Alloverse", emoji="🚧")
    async def build_alloverse_button(self, button, interaction: Interaction):
        next = BuildAlloverseAppStep(self)
        await interaction.send(next.message(), view=next, ephemeral=True)

    @nextcord.ui.button(label="File a bug or request a feature", emoji="🐞")
    async def file_a_bug_button(self, button, interaction: Interaction):
        await interaction.send(
            "🐛 Thanks! Ask around in #development or #feature-suggestions. You could also go straight to filing it in our Github issue tracking system.", 
            ephemeral=True
    )
    
    @nextcord.ui.button(label="Just look around", emoji="👀")
    async def just_looking_around_button(self, button, interaction: Interaction):
        await interaction.send(
            "💁 Okay then! That was always allowed!",
            ephemeral=True
        )
            

class BuildVrAppStep(IntroPage):
    def message(self):
        return "Great! Let's get you up and running! Do you have previous development experience?"

    @nextcord.ui.button(label="I'm kind of a newbie", emoji="👾")
    async def beginner(self, button, interaction: Interaction):
        await interaction.edit(
            content="Check out the Getting Started Guide to create your own app in a few minutes. You're also always welcome to ask questions in #support - we respond to all questions, no matter what level.",
            view=None
        )

    @nextcord.ui.button(label="3D Stuff", emoji="🫖")
    async def three_dee(self, button, interaction: Interaction):
        await interaction.response.edit_message(
            content="Super! Next stop: our documentation (which also houses a Getting Started Guide). See you in #app-developers!",
            view=None
        )

    @nextcord.ui.button(label="2D Stuff", emoji="🖼")
    async def two_dee(self, button, interaction: Interaction):
        await interaction.response.edit_message(
            content="Super! We wrote this blog post for people just like you! See you in #app-developers!",
            view=None
        )


class BuildAlloverseAppStep(IntroPage):
    def message(self):
        return "🤩 Wonderful! How would you like to help?"

    @nextcord.ui.button(label="Coding", emoji="👩‍💻")
    async def coding(self, button, interaction: Interaction):
        await interaction.edit(
            content="🤖 Whoa! Someone speaks my language! You'll feel right at home in #coding-alloverse :3",
            view=None
        )

    @nextcord.ui.button(label="Design", emoji="👩‍🎨")
    async def design(self, button, interaction: Interaction):
        await interaction.edit(
            content="🖌️ Fantastic! You'll love #product-design or #visual-design!",
            view=None
        )

    @nextcord.ui.button(label="Finiancial contributions", emoji="💰")
    async def design(self, button, interaction: Interaction):
        await interaction.edit(
            content="💰Wow! You're a hero. Bills needs a-paying. For financial contributions, please consider becoming a GitHub Sponsor.",
            view=None
        )

    @nextcord.ui.button(label="Discord Boosting", emoji="🔋")
    async def design(self, button, interaction: Interaction):
        await interaction.edit(
            content="💎 We'll gladly be on the receiving end of your generosity! In the top left corner of the Alloverse Discord, you'll find the button to boost.",
            view=None
        )

    @nextcord.ui.button(label="Spreading the word", emoji="📣")
    async def design(self, button, interaction: Interaction):
        await self.flow.complete(
            "📣 Helping us reach out to more users & contributors is extremely valuable - that's our focus over in the #marketing channel. Additionally, you can help make a difference simply by talking about Alloverse IRL, following us on social media and post using the hashtag #alloverse.",
            interaction
        )

    @nextcord.ui.button(label="Other", emoji="🌎")
    async def design(self, button, interaction: Interaction):
        await interaction.edit(
            content="⁉️ Oh, Interesting! Please reach out to tobi#4874 and we'll chat about it, ok?",
            view=None
        )

