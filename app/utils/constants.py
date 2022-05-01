import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)


BOT_TOKEN = os.getenv("BOT_TOKEN")

LOG_CHANNEL_ID = 970441093575487568
