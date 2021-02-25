from config import __BOT__
from random import random as rand


# Создал функцию, чтобы можно было прикрепить к стикеру ответ
def reply_with_sticker(message, sticker_id: str = None):
    return __BOT__.send_sticker(message.chat.id, sticker_id, reply_to_message_id=message.message_id)


# Решил уже и тут сделать отдельную функцию, ибо чтобы было в едином стиле
def reply_with_text(message, text: str):
    return __BOT__.reply_to(message, text)


# Вывод сообщения при получении команды "/start" или "/help"
@__BOT__.message_handler(commands=['start', 'help'], func=lambda message: True)
def send_welcome(message):
    reply_with_text(message, "Howdy, how are you doing?")


# Если приходит стикер - ответить стикером в ответ
@__BOT__.message_handler(func=lambda message: True, content_types=['sticker'])
def sticker_reply(message):
    n = round(rand() * 4)
    if n == 0:
        # Иди нахуй
        reply_with_sticker(message, 'CAACAgIAAxkBAAIgSWA3-6kDhEPXc76-aetU7AWmF-yLAAKPAAOMgEUSfLi37KtGpWgeBA')
    if n == 1:
        # Тебе меда или сразу по ебалу
        reply_with_sticker(message, 'CAACAgIAAxkBAAIhWWA4IEatwgABNJ93dIrxHNzaYScrawACmgADjIBFEiiUTEB1nq2nHgQ')
    if n == 2:
        # Пидарас
        reply_with_sticker(message, 'CAACAgIAAxkBAAIhWGA4H9n6_FOdgJcKkkPJ0AaRdNEvAAKXAAOMgEUSvBmWQqShtO4eBA')
    if n == 3:
        # Я вижу ты ахуел
        reply_with_sticker(message, 'CAACAgIAAxkBAAIhWmA4IHVfN9p01szCR-jZwJD9CpnOAAJlAAOMgEUSIRnIEE7mWjYeBA')
    if n == 4:
        # Тебя в детстве ебали?
        reply_with_sticker(message, 'CAACAgIAAxkBAAIgSmA3--ddAjN8ZRtau1wp3EccgtH-AAKbAAOMgEUSXhu5Q5FXG-0eBA')


def start_handing():
    __BOT__.polling()
