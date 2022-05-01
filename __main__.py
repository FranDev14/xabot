from app.utils.constants import BOT_TOKEN
from app.utils.bot import bot


def run():
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    run()
