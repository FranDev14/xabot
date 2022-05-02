import discord
import json
import requests
from discord.ext.commands import Bot, Cog, command
from discord.ext import tasks
from discord.utils import get
from os.path import join, dirname
from app.utils.constants import TW_SECRET, TW_CLIENT_ID, TW_ENDPOINT, TW_AUTH_ENDPOINT, TW_MESSAGE, TW_ROLE_ID, TW_CHANNEL, TW_GUILD


autparams = {'client_id': TW_CLIENT_ID,
             'client_secret': TW_SECRET,
             'grant_type': 'client_credentials'
             }


def check_user(user):
    try:
        aut_call = requests.post(url=TW_AUTH_ENDPOINT, params=autparams)
        access_token = aut_call.json()['access_token']

        header = {
            'Client-ID': TW_CLIENT_ID,
            'Authorization': "Bearer " + access_token
        }

        data = requests.get(TW_ENDPOINT.format(user), headers=header).json()

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
        self.streamers_json = join(dirname(__file__), '../configs/streamers.json')

    @Cog.listener()
    async def on_ready(self):
        self.bot.log.info("Twitch Plugin loaded")
        self.live_notification_loop.start()

    @tasks.loop(seconds=5.0)
    async def live_notification_loop(self):
        # Reload variables
        guild = await self.bot.fetch_guild(int(TW_GUILD))
        channel = await self.bot.fetch_channel(TW_CHANNEL)
        role = get(guild.roles, id=int(TW_ROLE_ID))

        with open(self.streamers_json, 'r') as file:
            streamers = json.loads(file.read())

        if streamers is not None:
            for user_id, twitch_name in streamers.items():
                status, data = check_user(twitch_name)
                test = await self.bot.fetch_user(user_id)
                print(str(status), str(data), str(test))


def setup(bot):
    bot.add_cog(TwitchBot(bot))
