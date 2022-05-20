from telebot import types

from ....config import BOT
from ....Utility import database as db
from ....Utility.message_helpers import reply_with_text, send_msg


@BOT.message_handler(commands=["start"])
def send_welcome(message: types.Message):
    """
    Answer welcome message to user, if it wrote "/start" or "/help"
    """
    db.add_new_user(message.from_user)
    reply_with_text(message, "Тринатцать")

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
