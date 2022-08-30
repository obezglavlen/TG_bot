from telebot import types

from ....config import BOT
from ....Utility import database as db
from ....Utility.message_helpers import reply_with_text, send_msg


@BOT.message_handler(commands=["start"])
def send_welcome(message: types.Message):
    """
    Answer welcome message to user, if it wrote "/start" or "/help"
    """
    if message.chat.type == "private" and not message.from_user.is_bot:
        db.add_new_user(message.from_user)
        send_contact_button = types.KeyboardButton(
            text="✉ Отправить номер (Опционально)", request_contact=True)
        cancel_button = types.KeyboardButton(text="❌ Отмена")

        def get_markup():
            markup = types.ReplyKeyboardMarkup()
            markup.row_width = 1
            markup.resize_keyboard = True
            markup.add(send_contact_button, cancel_button)

            return markup

        send_msg(message, "Для полной регистрации, отправьте свой контакт",
                 reply_markup=get_markup())

    elif message.chat.type in ["group", "supergroup"]:
      db.add_new_chat(message.chat.id)

    reply_with_text(message, "Тринатцать")