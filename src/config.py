import telebot
import os
import pymongo

TOKEN = os.environ.get("TELEGRAM_TOKEN")
MONGO = os.environ.get("MONGO_URL")
HEROKU = os.environ.get("HEROKU_URL")
PORT = int(os.environ.get("PORT", 5000))

BOT: telebot.TeleBot = telebot.TeleBot(TOKEN)
DB = pymongo.MongoClient(MONGO).tgDB


STICKERS: list = [
    "CAACAgIAAxkBAAIgSWA3-6kDhEPXc76-aetU7AWmF-yLAAKPAAOMgEUSfLi37KtGpWgeBA",
    "CAACAgIAAxkBAAIhWWA4IEatwgABNJ93dIrxHNzaYScrawACmgADjIBFEiiUTEB1nq2nHgQ",
    "CAACAgIAAxkBAAIhWGA4H9n6_FOdgJcKkkPJ0AaRdNEvAAKXAAOMgEUSvBmWQqShtO4eBA",
    "CAACAgIAAxkBAAIhWmA4IHVfN9p01szCR-jZwJD9CpnOAAJlAAOMgEUSIRnIEE7mWjYeBA",
    "CAACAgIAAxkBAAIgSmA3--ddAjN8ZRtau1wp3EccgtH-AAKbAAOMgEUSXhu5Q5FXG-0eBA",
]

RANDOM_PHRASES: list = [
    "phrase1",
    "phrase2",
    "phrase3",
    "phrase4",
    "phrase5",
]
