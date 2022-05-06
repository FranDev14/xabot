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


def setup(bot):
    bot.add_cog(General(bot))
