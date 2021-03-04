from telebot import types
from code.config import BOT


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
