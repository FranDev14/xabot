import logging
from discord.ext.commands import Bot, when_mentioned_or
from app.utils.logger import DiscordHandler

logger = logging.getLogger(__name__)

bot = Bot(command_prefix=when_mentioned_or("!"))

logger.addHandler(DiscordHandler(bot))
logger.setLevel(logging.INFO)

bot.log = logger

# Load Extensions
bot.load_extension("app.modules.general")
bot.load_extension("app.modules.commands")
bot.load_extension("app.modules.twitch")
