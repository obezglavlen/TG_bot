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


BOT.delete_my_commands(scope=None, language_code=None)
BOT.set_my_commands(
    commands=[
        telebot.types.BotCommand(command="start",
                                 description="Початок роботи з ботом та реєстрація"),
        telebot.types.BotCommand(command="help",
                                 description="Допомога"),
        telebot.types.BotCommand(command="random",
                                 description="Випадкове число"),
        telebot.types.BotCommand(command="randphrase",
                                 description="Випадкова фраза"),
        telebot.types.BotCommand(command="search",
                                 description="Пошук аніме по зображенню"),
        telebot.types.BotCommand(command="dick",
                                 description="Дікадуді"),
    ],
    scope=telebot.types.BotCommandScopeAllGroupChats()
)
BOT.set_my_commands(
    commands=[
        telebot.types.BotCommand(command="start",
                                         description="Початок роботи з ботом та реєстрація"),
        telebot.types.BotCommand(command="help",
                                 description="Допомога"),
        telebot.types.BotCommand(command="random",
                                 description="Випадкове число"),
        telebot.types.BotCommand(command="randphrase",
                                 description="Випадкова фраза"),
        telebot.types.BotCommand(command="search",
                                 description="Пошук аніме по зображенню"),
        telebot.types.BotCommand(command="dick",
                                 description="Дікадуді"),
        telebot.types.BotCommand(command="anime",
                                 description="Робота зі списками"),
    ],
    scope=telebot.types.BotCommandScopeAllPrivateChats()
)
