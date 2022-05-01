from src.config import BOT
from telebot.types import ReplyKeyboardRemove
from src.Utility.database import update_user_by_id
from src.message_handling.utility import send_msg, reply_with_text


@BOT.message_handler(func=lambda message: True, content_types=["contact"])
def handle_contact(message):
    """Handle contact message."""
    markup = ReplyKeyboardRemove()
    if message.from_user.id == message.contact.user_id:
        send_msg(message, "You send your contact", reply_markup=markup)
        update_user_by_id(message.from_user.id, {"number": message.contact.phone_number})
    else:
        reply_with_text(message, "You can't send contact of other user")


@BOT.message_handler(func=lambda message: True)
def handle_all_messages(message):
    """Handle all messages."""
    if message.text == "✉ Отправить номер":
        markup = ReplyKeyboardRemove()
        reply_with_text(message, "Вы успешно зарегестрированы", reply_markup=markup)
    elif message.text == "❌ Отмена":
        markup = ReplyKeyboardRemove()
        send_msg(message, "Регистрация отменена, не все функции будут доступны", reply_markup=markup)
