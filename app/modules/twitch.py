import discord
import logging
from discord.ext.commands import Bot, Cog, command
from discord.ext import tasks
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from app.utils.constants import TW_SECRET, TW_CLIENT_ID, TW_TOKEN, TW_REFRESH_TOKEN, TW_MESSAGE

twitch = Twitch(TW_CLIENT_ID, TW_SECRET)
target_scope = [AuthScope.BITS_READ]
twitch.set_user_authentication(TW_TOKEN, target_scope, TW_REFRESH_TOKEN)


def check_user(user):
    try:
        userid = twitch.get_users(logins=[user])['data'][0]['id']
        data = twitch.get_streams(user_id=userid)

        if not data['data']:
            return False, data
        elif data['data'][0]['type'] == "live":
            return True, data
        else:
            return False, data

    except Exception as e:
        print("Error checking user: ", e)


class TwitchBot(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        # @tasks.loop(seconds=10)
        print("test")


def setup(bot):
    bot.add_cog(TwitchBot(bot))
