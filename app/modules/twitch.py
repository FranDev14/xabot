import os.path

import discord
import json
import requests
from discord.ext.commands import Bot, Cog, command
from discord.ext import tasks
from discord.utils import get
from os.path import join, dirname
from app.utils.constants import TW_SECRET, TW_CLIENT_ID, TW_ENDPOINT, TW_AUTH_ENDPOINT, TW_ROLE_ID, TW_CHANNEL, TW_GUILD


autparams = {'client_id': TW_CLIENT_ID,
             'client_secret': TW_SECRET,
             'grant_type': 'client_credentials'
             }


def check_user(user):
    try:
        # Get the twitch token
        aut_call = requests.post(url=TW_AUTH_ENDPOINT, params=autparams)
        access_token = aut_call.json()['access_token']

        header = {
            'Client-ID': TW_CLIENT_ID,
            'Authorization': "Bearer " + access_token
        }

        # Get data from twitch
        data = requests.get(TW_ENDPOINT.format(user), headers=header).json()

        # If the channel not are on air false and if not return true
        if not data['data']:
            return False
        elif data['data'][0]['type'] == "live":
            return True
        else:
            return False

    except Exception as e:
        print("Error checking user: ", e)


class TwitchBot(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.streamers_json = join(dirname(__file__), '../configs/streamers.json')

    # When plugin loading, check if streamers.json exists and launch the notification task
    @Cog.listener()
    async def on_ready(self):
        self.bot.log.info("Twitch module loaded")
        print("Twitch plugin loaded")
        if not os.path.exists(self.streamers_json):
            with open(self.streamers_json, "w") as file:
                file.write(json.dumps({}, indent='\t'))

            self.live_notification_loop.start()
        else:
            self.live_notification_loop.start()

    @tasks.loop(minutes=5.0)
    async def live_notification_loop(self):
        # Get different variables from ID
        guild = await self.bot.fetch_guild(int(TW_GUILD))
        channel = await self.bot.fetch_channel(TW_CHANNEL)
        role = get(guild.roles, id=int(TW_ROLE_ID))

        # Open streamers JSON
        with open(self.streamers_json, 'r') as file:
            streamers = json.loads(file.read())

        if streamers is not None:
            # Search live channels
            for user_id, twitch_name in streamers.items():
                status = check_user(twitch_name)
                user = await self.bot.fetch_user(user_id)

                if status is True:
                    # Get the roles and assign Streamer role if are on air
                    async for member in guild.fetch_members(limit=None):
                        if member.id == int(user_id):
                            await member.add_roles(role)
                    # Send the notification to the discord channel
                    await channel.send(
                        f":red_circle: **LIVE** :red_circle:\n{user.mention} esta en directo! Pasate a saludar! @here"
                        f"\nhttps://www.twitch.tv/{twitch_name}")

                else:
                    # If user in the list not on air, remove Streamer role
                    async for member in guild.fetch_members(limit=None):
                        if member.id == int(user_id):
                            await member.remove_roles(role)

    @command(name='addtwitch', help='Añade un twitch al sistema de streamers', pass_context=True)
    async def add_twitch(self, ctx, user, twitch_name):
        # Get the user ID and open the Streamers json
        userID = discord.User = user
        with open(self.streamers_json, 'r') as file:
            streamers = json.loads(file.read())

        # Clean user ID
        userID = userID.replace("@", "")
        userID = userID.replace("<", "")
        userID = userID.replace(">", "")

        streamers[userID] = twitch_name

        # Write streamers into the json
        with open(self.streamers_json, 'w') as file:
            file.write(json.dumps(streamers, indent='\t'))

        # Send confirmation to the channel that send the command
        await ctx.send(f"Added {twitch_name} for {user} to the notification list")

    @command(name='removetwitch', help='Elimina un usuario de twitch del sistema de streamers', pass_context=True)
    async def remove_twitch(self, ctx, user):
        # Get the user ID
        userID = discord.User = user

        # Clean user ID
        userID = userID.replace("@", "")
        userID = userID.replace("<", "")
        userID = userID.replace(">", "")

        # Open the Streamers Json, remove the user and write it.
        with open(self.streamers_json, 'r') as file:
            streamers = json.loads(file.read())

        streamers.pop(userID)

        with open(self.streamers_json, 'w') as file:
            file.write(json.dumps(streamers, indent='\t'))

        # Send confirmation to the channel that send the command
        await ctx.send(f"Removed {user} from the notification list")


def setup(bot):
    bot.add_cog(TwitchBot(bot))
