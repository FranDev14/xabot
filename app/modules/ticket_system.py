import discord
from discord.ext.commands import Cog, Bot, command, has_role
from discord.utils import get
from app.utils.constants import GUILD_ID, TICKET_CATEGORY_NAME, TICKET_MOD_ROLE_ID, MANAGEMENT_ROLE
from discord_slash.utils.manage_components import ComponentContext, create_actionrow, create_button


class Ticket(Cog):
	def __init__(self, bot: Bot):
		self.bot = bot
		self.ticket_category = self.ticket_mod_role = self.management_role = self.guild = None

	@Cog.listener()
	async def on_ready(self):
		# Load variables
		self.guild = self.bot.get_guild(GUILD_ID)

		self.ticket_category = get(self.guild.categories, name=TICKET_CATEGORY_NAME)

		self.ticket_mod_role = self.guild.get_role(role_id=TICKET_MOD_ROLE_ID)

		self.management_role = self.guild.get_role(role_id=MANAGEMENT_ROLE)

		print("Ticket system plugin loaded")
		self.bot.log.info("Ticket system module loaded")

	@Cog.listener()
	async def on_component(self, ctx: ComponentContext):
		await ctx.defer(ignore=True)

		ticket_created = discord.Embed(
			title="Ticket Procesado",
			description=f"""Hey {ctx.author.name}! Gracias por abrir un ticket! Antes de ser transferido con un staff será revisado.
			Esto es para prevenir spam y que bots abran tickets aleatorios, por favor, describe tu problema brevemente. Gracias por su paciencia! :3"""
		)

		overwrites = {
			self.guild.default_role: discord.PermissionOverwrite(view_channel=False),
			ctx.author: discord.PermissionOverwrite(view_channel=True),
			self.guild.me: discord.PermissionOverwrite(view_channel=True),
			self.ticket_mod_role: discord.PermissionOverwrite(view_channel=True)
		}

		ticket = await self.ticket_category.create_text_channel(
			f"{ctx.author.name}-{ctx.author.discriminator}", overwrites=overwrites
		)

		await ticket.send(
			ctx.author.mention, embed=ticket_created
		)

	@command()
	@has_role(str(TICKET_MOD_ROLE_ID))
	async def sendticket(self, ctx):
		embed = discord.Embed(
			title="Soporte",
			description="Haz click en el botón para abrir un ticket"
		)

	@command(aliases=["approve"])
	@has_role(TICKET_MOD_ROLE_ID)
	async def up(self, ctx):
		overwrites = {
			ctx.guild.me: discord.PermissionOverwrite(view_channel=True),
			ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
			self.ticket_mod_role: discord.PermissionOverwrite(view_channel=None),
			self.management_role: discord.PermissionOverwrite(view_channel=True)
		}

		await ctx.channel.edit(overwrites=overwrites)

		await ctx.send(
			"Ticket aprobado!\nTu ticket ha sido transferido al Staff, serás asistido lo antes posible"
		)

	@command()
	@has_role(TICKET_MOD_ROLE_ID)
	async def close(self, ctx):
		try:
			if int(ctx.channel.name[-4]) > 0:
				await ctx.channel.delete()
			else:
				await ctx.send("❌ Esto no parece un canal para tickets")
		except:
			await ctx.send("❌ Esto no parece un canal para tickets")


def setup(bot):
	bot.add_cog(Ticket(bot))
