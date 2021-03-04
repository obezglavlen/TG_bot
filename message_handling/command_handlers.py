from message_handling.utility import reply_with_text
from config import BOT


# Вывод сообщения при получении команды "/start" или "/help"
@BOT.message_handler(commands=['start', 'help'], func=lambda message: True)
def send_welcome(message):
    """
    Answer welcome message to user, if it wrote '/start' or '/help'
    :param message: message object from bot
    """
    reply_with_text(message, "Howdy, how are you doing?")