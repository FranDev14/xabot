from discord.ext.commands import Bot, Cog
from discord import RawReactionActionEvent
from app.utils.constants import REACTION_JSON
from discord.utils import get


class General(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def get_values(self, payload, value):
        channel = await self.bot.fetch_channel(payload.channel_id)
        guild = self.bot.get_guild(payload.guild_id)
        user = await guild.fetch_member(payload.user_id)
        role = get(guild.roles, id=int(value))
        msg = await channel.fetch_message(str(payload.message_id))

        return channel, guild, user, role, msg

    async def process_reaction(self, payload: RawReactionActionEvent, r_type=None) -> None:
        try:
            if str(payload.message_id) in REACTION_JSON.keys():
                for key, value in REACTION_JSON[str(payload.message_id)].items():
                    if key == payload.emoji.name:
                        channel, guild, user, role, msg = await self.get_values(payload, value)

                        if role is None:
                            raise Exception('Invalid role ID')
                        elif r_type == "add":
                            await user.add_roles(role)
                            await msg.remove_reaction(key, user)

        except Exception as e:
            self.bot.log.error('Error found on: {}'.format(e))

    @Cog.listener()
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self.bot))
        print("General plugin loaded")
        self.bot.log.info("General module loaded")

    @Cog.listener()
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent):
        await self.process_reaction(payload, "add")

    @Cog.listener()
    async def on_raw_reaction_remove(self, payload: RawReactionActionEvent):
        await self.process_reaction(payload, "remove")


def setup(bot):
    bot.add_cog(General(bot))
