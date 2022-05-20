from telebot.types import ReplyKeyboardRemove

from ....config import BOT
from ....Utility.message_helpers import reply_with_text, send_msg


@BOT.message_handler(func=lambda message: True)
def handle_all_messages(message):
    """Handle all messages."""
    if message.text == "✉ Отправить номер":
        markup = ReplyKeyboardRemove()
        reply_with_text(message, "Вы успешно зарегестрированы",
                        reply_markup=markup)
    elif message.text == "❌ Отмена":
        markup = ReplyKeyboardRemove()
        send_msg(
            message, "Регистрация отменена, не все функции будут доступны", reply_markup=markup)
