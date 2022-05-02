import discord
import json
import requests
from discord.ext.commands import Bot, Cog, command
from discord.ext import tasks
from os.path import join, dirname
from app.utils.constants import TW_SECRET, TW_CLIENT_ID, TW_ENDPOINT, TW_AUTH_ENDPOINT, TW_MESSAGE, TW_NOTIFICATION_CHANNEL


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

        check_user('imxavik')

    @Cog.listener()
    async def on_ready(self):
        @tasks.loop(seconds=10)
        async def live_notification_loop():
            with open(self.streamers_json, 'r') as file:
                streamers = json.loads(file.read())

            if streamers is not None:
                print("Ha pasado")


def setup(bot):
    bot.add_cog(TwitchBot(bot))
