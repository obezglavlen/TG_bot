from src.message_handling.utility import reply_with_text
from src.config import BOT
from src.Utility.random import *


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
    argc = message.text.split(' ')[1:]

    if len(argc) > 2:
        reply_with_text(message, 'Too many arguments')
        return

    elif len(argc) == 1:
        try:
            int(argc[0])
        except ValueError:
            reply_with_text(message, 'Invalid arguments')
            return
        else:
            reply_with_text(message, get_random_number(int(argc[0])))
            return

    else:
        try:
            for arg in argc:
                int(arg)
        except ValueError:
            reply_with_text(
                message, 'Invalid arguments')
            return
        else:
            reply_with_text(
                message, get_random_number(int(argc[0]), int(argc[1])))
            return
