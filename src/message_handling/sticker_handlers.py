from src.config import BOT, STICKERS
from src.message_handling.utility import reply_with_sticker
from src.Utility.random import get_random_number


@BOT.message_handler(func=lambda message: True, content_types=['sticker'])
def sticker_reply(message):
    """
    If user send a sticker, bot reply on this message with a
    random sticker.
    To get another sticker from api you need to get log:
        print(message['sticker']['file_id'])

    :param message: message object from bot
    """
    n = get_random_number(4)
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
