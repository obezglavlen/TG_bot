from src.config import BOT, STICKERS
from src.message_handling.utility import reply_with_sticker
from random import choice


@BOT.message_handler(func=lambda message: True,
                     content_types=["sticker"],
                     chat_types=["private"]
                     )
def sticker_reply(message):
    """
    If user send a sticker, bot reply on this message with a
    random sticker.
    To get another sticker from api you need to get log:
        print(message["sticker"]["file_id"])

    :param message: message object from bot
    """
    reply_with_sticker(message, choice(list(STICKERS.values())))
