from ....config import BOT
from ....Utility.database import get_user_anime_by_user_id
from ....Utility.message_helpers import reply_with_text
from .title_handler import handle_anime_title


@BOT.callback_query_handler(func=lambda call: "cb_anime_category_liked" in call.data)
def handle_liked_category(call):
    if "cb_anime_add" in call.data:
        BOT.clear_step_handler_by_chat_id(call.message.chat.id)
        BOT.answer_callback_query(call.id, "Відправте назву аніме")
        BOT.register_next_step_handler(
            call.message, handle_anime_title, action="add", category="liked", call=call)
        return
    if "сb_anime_remove" in call.data:
        BOT.clear_step_handler_by_chat_id(call.message.chat.id)
        anime_list = get_user_anime_by_user_id(call.from_user.id, "liked")
        BOT.edit_message_text(
            message_id=call.message.message_id,
            chat_id=call.message.chat.id,
            text="\n".join(anime_list) if len(
                anime_list) else "Список порожній",
            reply_markup=call.message.reply_markup,
        )
        if len(anime_list):
            BOT.answer_callback_query(call.id, "Відправте назву аніме")
            BOT.register_next_step_handler(
                call.message, handle_anime_title, action="remove", category="liked", call=call)
        return
    if "cb_anime_categories" in call.data:
        BOT.clear_step_handler_by_chat_id(call.message.chat.id)
        BOT.answer_callback_query(call.id, "Перегляд списку улюблених")
        anime = get_user_anime_by_user_id(call.from_user.id, "liked")
        if len(anime):
            reply_with_text(call.message, "\n".join(anime))
        else:
            reply_with_text(call.message, "Список порожній")
        return
