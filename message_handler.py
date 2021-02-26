from config import BOT
from random import random as rand
from config import STICKERS
from telebot import types


# Создал функцию, чтобы можно было прикрепить к стикеру ответ
def reply_with_sticker(message: types.Message, sticker_id: str):
    """
    Overwrite method to reply on message with sticker

    :param message: message object from bot
    :param sticker_id: sticker id to send
    """
    BOT.send_sticker(message.chat.id, sticker_id,
                     reply_to_message_id=message.message_id)


# Решил уже и тут сделать отдельную функцию, ибо чтобы было в едином стиле
def reply_with_text(message: types.Message, text: str):
    """
    Overwrite method to reply on message with text

    :param message: message object from bot
    :param text: text to answer
    """
    BOT.reply_to(message, text)


# Вывод сообщения при получении команды "/start" или "/help"
@BOT.message_handler(commands=['start', 'help'], func=lambda message: True)
def send_welcome(message: str):
    """
    Answer welcome message to user, if it wrote '/start' or '/help'

    :param message: message object from bot
    """
    reply_with_text(message, "Howdy, how are you doing?")


# Если приходит стикер - ответить стикером в ответ
@BOT.message_handler(func=lambda message: True, content_types=['sticker'])
def sticker_reply(message: str):
    """
    If user send a sticker, bot reply on this message with a
    random sticker.
    To get another sticker from api you need to get log:
        print(message['sticker']['file_id'])

    :param message: message object from bot
    """
    n = round(rand() * 4)
    if n == 0:
        # Иди нахуй
        reply_with_sticker(message, STICKERS['go_fuck_urslf'])
    if n == 1:
        # Тебе меда или сразу по ебалу
        reply_with_sticker(message, STICKERS['honey_or_in_the_face'])
    if n == 2:
        # Пидарас
        reply_with_sticker(message, STICKERS['faggot'])
    if n == 3:
        # Я вижу ты ахуел
        reply_with_sticker(message, STICKERS['i_see_ur_fucked'])
    if n == 4:
        # Тебя в детстве ебали?
        reply_with_sticker(message, STICKERS['u_were_fucked_in_children'])


def start_handing():
    """
    Loop bot for stay alive
    """
    BOT.polling()
