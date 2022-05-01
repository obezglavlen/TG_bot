from src.message_handling import *
from src.config import BOT
from dotenv import load_dotenv
import os
from flask import Flask, request
from telebot.types import Update


# Load .env file
load_dotenv()

TOKEN = os.environ.get("TELEGRAM_TOKEN")
PORT = int(os.environ.get("PORT", 5000))
HEROKU_URL = os.environ.get("HEROKU_URL")
server = Flask(__name__)


@server.route("/" + TOKEN, methods=["POST"])
def getMessage():
    BOT.process_new_updates([Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    BOT.remove_webhook()
    BOT.set_webhook(url=HEROKU_URL + TOKEN, allowed_updates=["message"])
    return "!", 200


if __name__ == "__main__":
    # If you host bot on Heroku, you can use Flask server for webhook
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

    # If you host bot on localhost, you can use bot polling
    # BOT.remove_webhook()
    # BOT.polling(none_stop=True)
