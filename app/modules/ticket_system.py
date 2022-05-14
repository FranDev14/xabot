from discord.ext.commands import Cog, Bot
from app.utils.constants import TICKET_SYSTEM
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import ComponentContext, create_actionrow, create_button


class Ticket(Cog):
	def __init__(self, bot: Bot):
		self.bot = bot
		self.ticket_category = self.ticket_mod_role = self.management_role = self.guild = None

	@Cog.listener()
	async def on_ready(self):
		print("Ticket system plugin loaded")
		self.bot.log.info("Ticket system module loaded")


def setup(bot):
	bot.add_cog(Ticket(bot))
