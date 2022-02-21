import config, utils
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

    async def give_user_role(self, user: Member , role_id: int):
        role = user.guild.get_role(role_id)
        if role:
            await user.add_roles(role)
            await utils.log(user.guild, f"Gave {role.mention} to {user.mention}")
        else:
            await utils.log(user.guild, f"Failed to find role_id {role_id} for {user.mention}")

class IntroductionStep(IntroPage): #TODO: Add the current welcome/rules here
    def message(self):
        return f"💁 Now, what would you like to do?"

    @nextcord.ui.button(label="Build a VR App", emoji="🎁")
    async def build_vr_button(self, button, interaction: Interaction):
        await self.give_user_role(interaction.user, config.ROLE_APP_DEVELOPER)
        next = BuildVrAppStep(self)
        await interaction.send(next.message(), view=next, ephemeral=True)

    @nextcord.ui.button(label="Build the Alloverse Platform", emoji="🛠")
    async def build_alloverse_button(self, button, interaction: Interaction):
        await self.give_user_role(interaction.user, config.ROLE_PLATFORM_DEVELOPER)
        next = BuildAlloverseAppStep(self)
        await interaction.send(next.message(), view=next, ephemeral=True)

    @nextcord.ui.button(label="File a bug or feature", emoji="🐞")
    async def file_a_bug_button(self, button, interaction: Interaction):
        channel_suggestion = interaction.guild.get_channel(config.CHANNEL_FEATURE_SUGGESTION)
        channel_suggestion = (channel_suggestion and channel_suggestion.mention) or "#feature-suggestions"
        
        channel_coding = interaction.guild.get_channel(config.CHANNEL_CODING_ALLOVERSE)
        channel_coding = (channel_coding and channel_coding.mention) or "#coding-alloverse"
        
        await interaction.send(
            content="\n\n".join([
                f"🐞 Thanks! Please let us know in the {channel_coding} or {channel_suggestion} channels.",
                "If you want, you could also go straight to filing it yourself in our Github issue tracking system: https://github.com/orgs/alloverse/projects/1", 
            ]),
            ephemeral=True
    )
    
    @nextcord.ui.button(label="Just look around", emoji="👀")
    async def just_looking_around_button(self, button, interaction: Interaction):
        channel_announcements = interaction.guild.get_channel(config.CHANNEL_ANNOUNCEMENTS)
        channel_announcements = (channel_announcements and channel_announcements.mention) or "#announcements"

        channel_showcase = interaction.guild.get_channel(config.CHANNEL_SHOWCASE)
        channel_showcase = (channel_showcase and channel_showcase.mention) or "#showcase"

        await interaction.send(
            content="\n\n".join([
                "👀 Okay then! That was always allowed!",
                f"Check out {channel_announcements} for a quick look at the current state of Alloverse, or {channel_showcase} to see what others are building. Then, come say hi in the General voice- or text channels!"
            ]),
            ephemeral=True
        )


class BuildVrAppStep(IntroPage): #TODO: Temporarily simplify this step with a single path: Check out the getting started-guide and give 'em a channel or two to join.
    def message(self):
        return "Great! Let's get you up and running! Do you have previous development experience?"

    @nextcord.ui.button(label="I'm kind of a newbie", emoji="🐣")
    async def beginner(self, button, interaction: Interaction):
        channel_support = interaction.guild.get_channel(config.CHANNEL_SUPPORT)
        channel_support = (channel_support and channel_support.mention) or "#support"
        await interaction.send(
            content="\n\n".join([
                f"Check out the Getting Started Guide (https://docs.alloverse.com/) to create your own app in a few minutes. You're also always welcome to ask questions in {channel_support} - we respond to all questions, no matter what level.",
                "Oh, by the way! If you have teammates, let an Alloverse admin know and we'll create a dedicated channel for you to communicate!"
            ]),
            ephemeral=True
        )

    @nextcord.ui.button(label="3D Stuff", emoji="🫖")
    async def three_dee(self, button, interaction: Interaction):
        channel = interaction.guild.get_channel(config.CHANNEL_APP_DEVELOPERS)
        channel = (channel and channel.mention) or "#app-developers"
        await interaction.send(
            content="\n\n".join([
                f"🫖 Super! Next stop: our documentation (which also houses a Getting Started Guide). See you in {channel}!",
                "Oh, by the way! If you have teammates, let an Alloverse admin know and we'll create a dedicated channel for you to communicate!"
            ]),
            ephemeral=True
        )

    @nextcord.ui.button(label="2D Stuff", emoji="🖼")
    async def two_dee(self, button, interaction: Interaction):
        channel = interaction.guild.get_channel(config.CHANNEL_APP_DEVELOPERS)
        channel = (channel and channel.mention) or "#app-developers"
        await interaction.send(
            content="\n\n".join([
                f"Super! We wrote this blog post for people just like you! See you in {channel}!",
                "Oh, by the way! If you have teammates, let an Alloverse admin know and we'll create a dedicated channel for you to communicate!",
            ]),
            ephemeral=True
        )


class BuildAlloverseAppStep(IntroPage):
    def message(self):
        return "🛠 Wonderful! How would you like to help?"

    @nextcord.ui.button(label="Coding", emoji="👩‍💻")
    async def coding(self, button, interaction: Interaction):
        await self.give_user_role(interaction.user, config.ROLE_PROGRAMMER)
        channel_allocoding = interaction.guild.get_channel(config.CHANNEL_CODING_ALLOVERSE)
        channel_allocoding = (channel_allocoding and channel_allocoding.mention) or "#coding-alloverse"
        await interaction.send(
            content="\n\n".join([
                f"👩‍💻 Fabulous! You'll feel right at home in {channel_allocoding}!",
                "👉 Check out the beginner-friendly programming tasks in GitHub: https://github.com/orgs/alloverse/projects/" #TODO: Update with a proper URL
            ]),
            # embed=nextcord.Embed(title="👉 To get started, check out the current programming tasks in GitHub!", url="https://github.com/orgs/alloverse/projects/1"),
            ephemeral=True
        )

    @nextcord.ui.button(label="Design", emoji="👨‍🎨")
    async def design(self, button, interaction: Interaction):
        await self.give_user_role(interaction.user, config.ROLE_DESIGNER)
        channel_prod = interaction.guild.get_channel(config.CHANNEL_APP_DEVELOPERS)
        channel_prod = (channel_prod and channel_prod.mention) or "#product-design"
        channel_vis = interaction.guild.get_channel(config.CHANNEL_APP_DEVELOPERS)
        channel_vis = (channel_vis and channel_vis.mention) or "#visual-design"
        await interaction.send(
            content="\n\n".join([
                f"👨‍🎨 Fantastic! You'll love {channel_prod} or {channel_vis}!",
                "👉 Check out the current beginner-friendly design tasks in GitHub: https://github.com/orgs/alloverse/projects/" #TODO: Update with a proper URL
            ]),
            # embed=nextcord.Embed(title="👉 To get started, check out the current design tasks in GitHub!", url="https://github.com/orgs/alloverse/projects/1"),
            ephemeral=True
        )

    @nextcord.ui.button(label="Financial contributions", emoji="💰")
    async def financial(self, button, interaction: Interaction):
        await interaction.send(
            content="\n\n".join([
                "💰 Wow! You're a hero. Bills needs a-paying. For financial contributions, please consider becoming a GitHub Sponsor.",
            ]),
            ephemeral=True
        )

    @nextcord.ui.button(label="Discord Boosting", emoji="💎")
    async def boosting(self, button, interaction: Interaction):
        await interaction.send(
            content="\n\n".join([
                "💎 We'll gladly be on the receiving end of your generosity! In the top left corner of the Alloverse Discord, you'll find the button to boost.",
            ]),
            ephemeral=True
        )

    @nextcord.ui.button(label="Spreading the word", emoji="📣")
    async def marketing(self, button, interaction: Interaction):
        channel_marketing = interaction.guild.get_channel(config.CHANNEL_MARKETING)
        channel_marketing = (channel_marketing and channel_marketing.mention) or "#marketing"

        # channel_alloverse = interaction.guild.get_channel(config.CHANNEL_CODING_ALLOVERSE)
        # channel_alloverse = (channel_alloverse and channel_alloverse.mention) or "#alloverse"
        await interaction.send(
            content="\n\n".join([
                f"📣 Helping us reach out to more users & contributors is extremely valuable - that's our focus over in the {channel_marketing} channel.",
                "Additionally, you can help make a difference simply by talking about Alloverse IRL, following us on social media and post using the hashtag `#alloverse`.",
            ]),
            ephemeral=True
        )

    @nextcord.ui.button(label="Other", emoji="🤔")
    async def other(self, button, interaction: Interaction):
        user_tobi = interaction.client.get_user(config.USER_TOBI)
        user_tobi = user_tobi and f"to {user_tobi.mention}"
        await interaction.send(
            content="\n\n".join([
                f"🤔 Oh, interesting! Please reach out {user_tobi} and we'll chat about it, ok?",
            ]),
            ephemeral=True
        )

