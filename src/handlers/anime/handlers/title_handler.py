import re

from telebot import types

from ....config import BOT
from ....Utility.database import update_user_anime
from ....Utility.message_helpers import reply_with_text


def handle_anime_title(message: types.Message, action: str, category: str, call: types.CallbackQuery = None):
    if not message.content_type == "text":
        reply_with_text(message, "Введіть назву аніме")
        BOT.register_next_step_handler(
            message, handle_anime_title, action=action, category=category, call=call)
        return
    if message.text == "/cancel":
        return
    # replace all spaces with underscores and split by newline using regex
    anime_titles = [re.sub(" +", " ", anime).strip()
                    for anime in re.split(r"\n+", message.text)]

    updated = update_user_anime(
        message.from_user.id, anime_titles, action, category)

    match action:
        case "add":
            reply_with_text(
                message, f"Додання аніме... {updated}. Додано {len(updated)} з {len(anime_titles)} аніме")
        case "remove":
            BOT.edit_message_text(
                message_id=call.message.message_id,
                chat_id=call.message.chat.id,
                text="Видалення аніме зі списку...",
                reply_markup=call.message.reply_markup,
            )
            reply_with_text(message, f"Видалено {updated}. Видалено {len(updated)} з {len(anime_titles)} аніме" if
                            len(updated) else "Аніме не знайдено")
