from ....config import BOT
from ....Utility.animelist import main_menu_keyboard


@BOT.callback_query_handler(func=lambda call: "cb_anime_back" == call.data)
def handle_back_to_main(call):
    BOT.edit_message_text(
        message_id=call.message.message_id,
        chat_id=call.message.chat.id,
        text="Виберіть дію:",
        reply_markup=main_menu_keyboard(),
    )
