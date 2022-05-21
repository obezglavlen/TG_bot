from ....config import BOT
from ....Utility.animelist import main_menu_keyboard
from ....Utility.message_helpers import reply_with_text, send_msg
from ....Utility.database import setup_user_anime


@BOT.message_handler(commands=["anime"])
def hadle_anime_list(message):
    """Handle /anime command and send keyboard with buttons for navigate"""
    if message.chat.type != "private" and message.from_user.is_bot:
        reply_with_text(
            message, "Цю команду можна використовувати тільки в приватному чаті")
        return

    setup_user_anime(message.from_user.id)

    answer_message = send_msg(message, "Виберіть дію:")

    markup = main_menu_keyboard()

    BOT.edit_message_reply_markup(
        chat_id=message.chat.id, message_id=answer_message.message_id, reply_markup=markup)
