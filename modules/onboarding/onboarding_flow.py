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

class IntroductionStep(IntroPage):
    def message(self):
        welcomemsg = "\n\n".join([
            f"🎉 Hello, fellow VR enthusiast! How nice of you to join us!",
            "**Alloverse is the open source metaverse - created with, by and for its users**. Very simply put, it's a collection of virtual worlds, furnished with user-created virtual apps to support collaboration, play and personal connections.",
            "We believe AR and VR are here to stay, much like how smartphone apps and IOT devices became the next generation of what we once knew to be \"the Internet\". Our aim is to sideline the large corporations' closed-platform Metaverse (think: the next generation of the Android & iOS ecosystems), in favor of providing an *open* standard for the future of the immersive collaboration.",
            "The primary purpose of this Discord server is to support AlloApp developers and discuss the evolution of the Alloverse platform."
            "That said, the Alloverse community is open for discussing **any and all VR and AR endeavours** - such as the sharing of studies, use cases, UX/UI design and tips on how to code stuff for use in three dimensions. We're grateful for all support, feedback and contributions. Again, thanks for stopping by!",
            "💁 **Now, how would you like to get started?**"
        ])
        return welcomemsg

    @nextcord.ui.button(label="Build a VR App", emoji="🎁")
    async def build_vr_button(self, button, interaction: Interaction):
        await self.give_user_role(interaction.user, config.ROLE_APP_DEVELOPER)
        # next = BuildVrAppStep(self)
        # await interaction.send(next.message(), view=next, ephemeral=True)
        channel_support = interaction.guild.get_channel(config.CHANNEL_SUPPORT)
        channel_support = (channel_support and channel_support.mention) or "#support"
        buildVrAppMessage = "\n\n".join([
            "Great! Let's get you up and running!",
            f"Check out the Getting Started Guide (https://docs.alloverse.com/) to create your own app in a few minutes. You're also always welcome to ask questions in {channel_support} - we respond to all questions, no matter what level.",
            "Oh, by the way! If you have teammates, let an Alloverse admin know and we'll create a dedicated channel for you to communicate!"
        ])
        await interaction.send(
            content = buildVrAppMessage,
            # content="\n\n".join([
            #     f"🐞 Thanks! Please let us know in the {channel_coding} or {channel_suggestion} channels.",
            #     "If you want, you could also go straight to filing it yourself in our Github issue tracking system: https://github.com/orgs/alloverse/projects/1", 
            # ]),
            ephemeral=True
        )

    @nextcord.ui.button(label="Contribute to the Alloverse Platform", emoji="🛠")
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
                f"🐞 Thanks! Please let us know in the {channel_coding} or {channel_suggestion} channels!",
                "If you want, you could also go straight to filing it yourself in our Github issue tracking system: https://github.com/alloverse/allovisor/issues/new", 
            ]),
            ephemeral=True
        )
    
    @nextcord.ui.button(label="Just look around", emoji="👀")
    async def just_looking_around_button(self, button, interaction: Interaction):
        channel_announcements = interaction.guild.get_channel(config.CHANNEL_ANNOUNCEMENTS)
        channel_announcements = (channel_announcements and channel_announcements.mention) or "#announcements"

        channel_showcase = interaction.guild.get_channel(config.CHANNEL_SHOWCASE)
        channel_showcase = (channel_showcase and channel_showcase.mention) or "#showcase"

        channel_general = interaction.guild.get_channel(config.CHANNEL_GENERAL)
        channel_general = (channel_general and channel_general.mention) or "#general"

        await interaction.send(
            content="\n\n".join([
                "👀 Okay then! That was always allowed!",
                f"You're welcome to check out any channel you want, but a good start would be to introduce yourself in {channel_general}. Then, head over to {channel_announcements} for a quick look at the current state of Alloverse, or {channel_showcase} to see what others are building."
            ]),
            ephemeral=True
        )


class BuildVrAppStep(IntroPage):
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
        return "🛠 **Wonderful! How would you like to help?**"

    @nextcord.ui.button(label="Coding", emoji="👩‍💻")
    async def coding(self, button, interaction: Interaction):
        await self.give_user_role(interaction.user, config.ROLE_PROGRAMMER)
        channel_allocoding = interaction.guild.get_channel(config.CHANNEL_CODING_ALLOVERSE)
        channel_allocoding = (channel_allocoding and channel_allocoding.mention) or "#coding-alloverse"
        await interaction.send(
            content="\n\n".join([
                f"👩‍💻 Fabulous! You'll feel right at home in {channel_allocoding}!",
                "👉 Check out our current coding tasks in GitHub: https://github.com/orgs/alloverse/projects/2/views/6"
            ]),
            # embed=nextcord.Embed(title="👉 To get started, check out the current programming tasks in GitHub!", url="https://github.com/orgs/alloverse/projects/1"),
            ephemeral=True
        )

    @nextcord.ui.button(label="Design", emoji="👨‍🎨")
    async def design(self, button, interaction: Interaction):
        await self.give_user_role(interaction.user, config.ROLE_DESIGNER)
        channel_prod_design = interaction.guild.get_channel(config.CHANNEL_PRODUCT_DESIGN)
        channel_prod_design = (channel_prod_design and channel_prod_design.mention) or "#product-design"
        channel_visual_design = interaction.guild.get_channel(config.CHANNEL_VISUAL_DESIGN)
        channel_visual_design = (channel_visual_design and channel_visual_design.mention) or "#visual-design"
        await interaction.send(
            content="\n\n".join([
                f"👨‍🎨 Fantastic! You'll love {channel_prod_design} or {channel_visual_design}!",
                "👉 Check out our current design tasks in GitHub: https://github.com/orgs/alloverse/projects/2/views/5"
            ]),
            # embed=nextcord.Embed(title="👉 To get started, check out the current design tasks in GitHub!", url="https://github.com/orgs/alloverse/projects/1"),
            ephemeral=True
        )

    @nextcord.ui.button(label="Financial contributions", emoji="💰")
    async def financial(self, button, interaction: Interaction):
        await interaction.send(
            content="\n\n".join([
                "💰 Thank you! The simplest way to support us financially is to become a GitHub Sponsor: https://github.com/sponsors/alloverse. All contributions go toward the continous development of Alloverse.",
            ]),
            ephemeral=True
        )

    @nextcord.ui.button(label="Discord Boosting", emoji="💎")
    async def boosting(self, button, interaction: Interaction):
        await interaction.send(
            content="\n\n".join([
                "💎 We appreciate your support! More boosts means more visibility and perks for Alloverse. The button can be found in the top left corner, under the server name. Thanks a lot!",
            ]),
            ephemeral=True
        )

    @nextcord.ui.button(label="Spreading the word", emoji="📣")
    async def marketing(self, button, interaction: Interaction):
        channel_marketing = interaction.guild.get_channel(config.CHANNEL_MARKETING)
        channel_marketing = (channel_marketing and channel_marketing.mention) or "#marketing"
        await interaction.send(
            content="\n\n".join([
                f"📣 Helping us reach out to more users & contributors is extremely valuable - that's our focus over in the {channel_marketing} channel.",
                "Additionally, you can help make a difference simply by talking about Alloverse IRL, following us on social media and post using the hashtag `#alloverse`.",
            ]),
            ephemeral=True
        )

    @nextcord.ui.button(label="Other", emoji="👽")
    async def other(self, button, interaction: Interaction):
        user_tobi = interaction.client.get_user(config.USER_TOBI)
        user_tobi = user_tobi and f"to {user_tobi.mention}"
        await interaction.send(
            content="\n\n".join([
                f"👽 Oh, cool, we'd love to hear about it! Reach out to {user_tobi} and let's talk about it, ok?",
            ]),
            ephemeral=True
        )

