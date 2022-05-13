from discord.ext.commands import Bot, Cog, command
from app.utils.constants import RCON_PASS, RCON_PORT, RCON_IP
from rcon.source import rcon


class Rcon(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("Rcon plugin loaded")
        self.bot.log.info("Rcon module loaded")

    @command(name='broadcast')
    async def send_broadcast(self, ctx):
        await rcon('broadcast', str(ctx.message.content.replace("!broadcast ", "")), host=RCON_IP, port=RCON_PORT, passwd=RCON_PASS)
        self.bot.log.info("{} has sent an announcement to the server".format(ctx.message.author.mention))

    @command(name='save')
    async def send_saveworld(self, ctx):
        await rcon('saveworld', host=RCON_IP, port=RCON_PORT, passwd=RCON_PASS)
        self.bot.log.info("{} has saved the world".format(ctx.message.author.mention))

    @command(name='clean_dinos')
    async def send_cleandinos(self, ctx):
        await rcon('DestroyWildDinos', host=RCON_IP, port=RCON_PORT, passwd=RCON_PASS)
        self.bot.log.info("{} clean all dinosaurs on the map".format(ctx.message.author.mention))


def setup(bot):
    bot.add_cog(Rcon(bot))
