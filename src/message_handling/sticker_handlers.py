from src.config import BOT, STICKERS
from src.message_handling.utility import reply_with_sticker
from random import choice
from telebot import types


@BOT.message_handler(func=lambda message: True, content_types=["sticker"], chat_types=["private"])
def sticker_reply(message: types.Message):
    """Reply with random sticker

    Args:
        message (types.Message): message object
    """
    reply_with_sticker(message, choice(STICKERS))
