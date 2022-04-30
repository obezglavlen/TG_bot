import telebot
import os
import pymongo

TOKEN = os.environ.get("TELEGRAM_TOKEN")
MONGO = os.environ.get("MONGO_URL")

# Объект бота
BOT: telebot.TeleBot = telebot.TeleBot(TOKEN)


STICKERS: dict = {
    "go_fuck_urslf": "CAACAgIAAxkBAAIgSWA3-6kDhEPXc76-aetU7AWmF-yLAAKPAAOMgEUSfLi37KtGpWgeBA",
    "honey_or_in_the_face": "CAACAgIAAxkBAAIhWWA4IEatwgABNJ93dIrxHNzaYScrawACmgADjIBFEiiUTEB1nq2nHgQ",
    "faggot": "CAACAgIAAxkBAAIhWGA4H9n6_FOdgJcKkkPJ0AaRdNEvAAKXAAOMgEUSvBmWQqShtO4eBA",
    "i_see_ur_fucked": "CAACAgIAAxkBAAIhWmA4IHVfN9p01szCR-jZwJD9CpnOAAJlAAOMgEUSIRnIEE7mWjYeBA",
    "u_were_fucked_in_children": "CAACAgIAAxkBAAIgSmA3--ddAjN8ZRtau1wp3EccgtH-AAKbAAOMgEUSXhu5Q5FXG-0eBA",
}

RANDOM_PHRASES: list = ["Я ебал твою мать", "Прочесать снизу", "Оиииджоскеееее"]


DB = pymongo.MongoClient(MONGO).tgDB
