from telebot.types import ReplyKeyboardRemove

from ....config import BOT
from ....Utility.database import update_user_by_id
from ....Utility.message_helpers import reply_with_text, send_msg


@BOT.message_handler(func=lambda message: True, content_types=["contact"])
def handle_contact(message):
    """Handle contact message."""
    markup = ReplyKeyboardRemove()
    if message.from_user.id == message.contact.user_id:
        send_msg(message, "You send your contact", reply_markup=markup)
        update_user_by_id(message.from_user.id, {
                          "number": message.contact.phone_number})
    else:
        reply_with_text(message, "You can't send contact of other user")
