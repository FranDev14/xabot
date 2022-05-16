import logging
import discord
from discord.ext.commands import Bot, when_mentioned_or
from app.utils.logger import DiscordHandler
from discord_slash import SlashCommand

logger = logging.getLogger(__name__)
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = Bot(command_prefix=when_mentioned_or("!"), intents=intents)
slash = SlashCommand(bot)

logger.addHandler(DiscordHandler(bot))
logger.setLevel(logging.INFO)

bot.log = logger

# Load Extensions
bot.load_extension("app.utils.slash")
bot.load_extension("app.modules.general")
bot.load_extension("app.modules.commands")
bot.load_extension("app.modules.twitch")
bot.load_extension("app.modules.rcon")
bot.load_extension("app.modules.ticket_system")
