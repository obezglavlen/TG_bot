from code.message_handling.utility import reply_with_text
from code.config import BOT
from code.Utility.random import *


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
    argc = message.text.split(' ')[1: ]
    reply_with_text(message, get_random_number(argc))
