from random import choice

from telebot import types

from ....config import BOT, STICKERS
from ....Utility.message_helpers import reply_with_sticker


@BOT.message_handler(func=lambda message: True, content_types=["sticker"], chat_types=["private"])
def sticker_reply(message: types.Message):
    """Reply with random sticker

    Args:
        message (types.Message): message object
    """
    reply_with_sticker(message, choice(STICKERS))
