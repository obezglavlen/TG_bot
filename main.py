from src.message_handling import *
from src.config import BOT, TOKEN, PORT, HEROKU
from dotenv import load_dotenv
from flask import Flask, request
from telebot.types import Update, BotCommand


# Load .env file
load_dotenv()
server = Flask(__name__)


@server.route("/" + TOKEN, methods=["POST"])
def getMessage():
    BOT.process_new_updates(
        [Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    BOT.remove_webhook()
    BOT.set_webhook(url=HEROKU + TOKEN,
                    allowed_updates=["message", "callback_query"])
    return "!", 200


if __name__ == "__main__":
    # If you host bot on Heroku, you can use Flask server for webhook
    # server.run(host="0.0.0.0", port=PORT)

    # If you host bot on localhost, you can use bot polling
    BOT.remove_webhook()
    BOT.infinity_polling(allowed_updates=["message", "callback_query"])
