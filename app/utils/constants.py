from os.path import join, dirname
import json

config_file = join(dirname(__file__), '../configs/config.json')

with open(config_file, 'r') as file:
    config = json.loads(file.read())

# Discord
BOT_TOKEN = config['bot_config']['bot_token']
LOG_CHANNEL_ID = int(config['bot_config']['log_channel'])

# Channel IDs
WELCOME_CHANNEL_ID = int(config['discord_channels']['welcome_channel'])
TW_CHANNEL = int(config['discord_channels']['twitch_channel'])
HELP_CHANNEL = int(config['discord_channels']['help_channel'])
ANOUNCES = int(config['discord_channels']['announces_channel'])

# Twitch Config
TW_CLIENT_ID = config['twitch_live']['clientID']
TW_SECRET = config['twitch_live']['secretKey']
TW_ENDPOINT = config['twitch_live']['api_helix']
TW_AUTH_ENDPOINT = config['twitch_live']['auth_point']

# Messages
WEL_MESSAGE = config['messages']['welcome'].format(HELP_CHANNEL)

# Roles and Server
TW_ROLE_ID = int(config['discord_ids']['streamer_role'])
TW_GUILD = int(config['twitch_live']['guild_id'])
ANOUNCES_ROLE_EVENT = int(config['discord_ids']['event_role'])
ANOUNCES_ROLE_SHOP = int(config['discord_ids']['shop_role'])

# Rcon module
RCON_IP = str(config['rcon']['ip'])
RCON_PASS = str(config['rcon']['pass'])
RCON_PORT = int(config['rcon']['port'])

# Emoji reaction
REACTION_JSON = config['reaction_roles']
TICKET_SYSTEM = config['ticket_system']
