from discord.ext.commands import Bot, Cog


class General(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self.bot))
        print("General plugin loaded")
        self.bot.log.info("General module loaded")


def setup(bot):
    bot.add_cog(General(bot))
