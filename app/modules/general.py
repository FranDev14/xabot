import discord
from discord.ext.commands import Bot, Cog
from app.utils.constants import WELCOME_CHANNEL_ID, WEL_MESSAGE


class General(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self.bot))
        self.bot.log.info(
            "XaBot bot is ready"
        )

    @Cog.listener()
    async def on_member_join(self, member):
        self.bot.log.info("General Plugin loaded")
        join_channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
        join_msg = await join_channel.send(f"{member.mention}, {WEL_MESSAGE}")
        await join_msg.add_reaction('👋')


def setup(bot):
    bot.add_cog(General(bot))
