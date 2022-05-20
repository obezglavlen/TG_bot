from ....config import BOT
from ....Utility.animelist import categories_menu_keyboard


@BOT.callback_query_handler(func=lambda call: "cb_anime_add" == call.data)
def handle_add_anime(call):
    BOT.edit_message_text(
        message_id=call.message.message_id,
        chat_id=call.message.chat.id,
        text="Додання аніме до списку...",
        reply_markup=categories_menu_keyboard("cb_anime_add"),
    )


@BOT.callback_query_handler(func=lambda call: "cb_anime_remove" == call.data)
def handle_remove_anime(call):
    BOT.edit_message_text(
        message_id=call.message.message_id,
        chat_id=call.message.chat.id,
        text="Видалення аніме зі списку...",
        reply_markup=categories_menu_keyboard("сb_anime_remove"),
    )


@BOT.callback_query_handler(func=lambda call: "cb_anime_categories" == call.data)
def handle_show_anime(call):
    BOT.edit_message_text(
        message_id=call.message.message_id,
        chat_id=call.message.chat.id,
        text="Перегляд списків ...",
        reply_markup=categories_menu_keyboard("cb_anime_categories"),
    )
