from src.message_handling.utility import reply_with_text
from src.config import BOT
from src.Utility.random import *
import re


# Вывод сообщения при получении команды "/start" или "/help"
@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    Answer welcome message to user, if it wrote '/start' or '/help'
    :param message: message object from bot
    """
    reply_with_text(message, "Howdy, how are you doing?")


@BOT.message_handler(commands=['random'])
def random_number(message):
    args = re.split(' +', message.text)[1:]
    print(args)

    if len(args) > 2 or len(args) < 1:
        reply_with_text(message, '1 or 2 arguments only')
        return

    try:
        args = list(map(int, args))
    except ValueError:
        reply_with_text(
            message, 'Invalid arguments')
        return

    if len(args) == 1:
        reply_with_text(message, get_random_number(args[0]))
        return

    else:
        reply_with_text(message, get_random_number(args[0], args[1]))
        return
