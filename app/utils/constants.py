import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

# Discord
BOT_TOKEN = os.getenv("BOT_TOKEN")

LOG_CHANNEL_ID = 970441093575487568
WELCOME_CHANNEL_ID = 970342175290298368
WEL_MESSAGE = ("Bienvenido al servidor! Antes de empezar, porfavor leete las normas "
               "en #{}. Una vez leidas, aceptalas reaccionando a su mensaje!".format(os.getenv("HELP_CHANNEL")))

# TwitchAPI
TW_CLIENT_ID = os.getenv("CLIENT_ID")
TW_SECRET = os.getenv("SECRET_KEY")
TW_ENDPOINT = os.getenv("TW_ENDPOINT")
TW_AUTH_ENDPOINT = os.getenv("TW_AUTH_ENDPOINT")
TW_MESSAGE = ("Hola! @everyone {} esta en directo! Pasate y saluda!")
TW_NOTIFICATION_CHANNEL = os.getenv("TW_NOTIFICATION_CHANNEL")
