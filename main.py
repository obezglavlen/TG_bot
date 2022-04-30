from src.message_handling import *
from src.config import BOT
from dotenv import load_dotenv
import os
from flask import Flask, request
from telebot.types import Update


load_dotenv()
TOKEN = os.environ.get("TELEGRAM_TOKEN")
server = Flask(__name__)


@server.route("/" + TOKEN, methods=["POST"])
def getMessage():
    BOT.process_new_updates([Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    BOT.remove_webhook()
    BOT.set_webhook(url="https://flask-lapis-tg-bot.herokuapp.com/" + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    # BOT.remove_webhook()
    # BOT.polling(none_stop=True)
