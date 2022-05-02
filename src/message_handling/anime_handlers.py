from src.message_handling.utility import (
    reply_with_text,
    reply_with_video,
    anime_from_anilist,
)
import requests
from src.config import BOT, TOKEN
from src.Utility.animelist import menus
from src.Utility.database import update_user_anime, get_user_anime_by_user_id
import re


def filter_anime(anime: list):
    """Filter anime from list

    Args:
        anime (list): list of anime

    Returns:
        list: filtered anime list
    """
    used_anilists = []
    filtered_results = []
    for result in anime:
        if result["anilist"] not in used_anilists:
            used_anilists.append(result["anilist"])
            if result["similarity"] > 0.9:
                filtered_results.append(result)

    return filtered_results


def anime_search(message):
    file_id = ""
    if message.video:
        if message.video.file_size > 5000000:
            reply_with_text(message, "Слишком большой файл")
            return
        file_id = message.video.file_id
    elif message.animation:
        file_id = message.animation.file_id
    elif message.photo:
        file_id = message.photo[-1].file_id
    file_path = BOT.get_file(file_id).file_path
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    api_url = "https://api.trace.moe/search?{}".format(
        "&".join(
            [
                f"uid=tg{message.from_user.id}",
                f"url={file_url}",
                "cutBorders=1",
            ]
        )
    )
    search_result = None
    try:
        search_result = requests.get(api_url)
    except Exception:
        reply_with_text(
            message, "trace.moe API error, please try again later.")
        return

    if not search_result:
        reply_with_text(
            message, "trace.moe API error, please try again later.")
        return
    if search_result.status_code in [502, 503, 504]:
        reply_with_text(
            message, "trace.moe server is busy, please try again later.")
        return
    if search_result.status_code in [402, 429]:
        reply_with_text(
            message,
            "You exceeded the search limit, please try again later",
        )
        return
    if search_result.status_code >= 400:
        reply_with_text(
            message, "trace.moe API error, please try again later.")
        return

    search_result = search_result.json()

    if search_result["error"]:
        reply_with_text(
            message, "trace.moe API error, please try again later.")
        return
    if len(search_result["result"]) <= 0:
        reply_with_text(message, "No anime found")
        return

    search_result = filter_anime(search_result["result"])
    if len(search_result) <= 0:
        reply_with_text(message, "No anime found")
        return

    for result in search_result[:3]:

        anilist = result["anilist"]
        similarity = result["similarity"]
        video = result["video"]

        anime = None
        try:
            anime = anime_from_anilist(anilist)
        except Exception:
            reply_with_text(
                message, "Anilist API error, please try again later.")
            return

        if not anime:
            reply_with_text(
                message, "Anilist API error, please try again later.")
            return

        n = "\n"

        reply_message = (
            f"{anime['title']['romaji'] + ' | ' if anime['title']['romaji'] else ''}"
            f"{anime['title']['english'] + ' | ' if anime['title']['english'] else ''}"
            f"{anime['title']['native'] if anime['title']['native'] else ''}"
            "\n"
            f"{f'❗Adult content❗{n}' if anime['isAdult'] else ''}"
            f"Similarity: {similarity}\n"
        )

        reply_with_text(message, reply_message) if anime["isAdult"] else reply_with_video(
            message, video, reply_message
        )
    return


# Handling Select option callback
@BOT.callback_query_handler(func=lambda call: call.data == "cb_anime_add")
def handle_add_anime(call):
    BOT.edit_message_text(
        message_id=call.message.message_id,
        chat_id=call.message.chat.id,
        text="Додання аніме до списку...",
        reply_markup=menus["add_menu"]("cb_anime_add"),
    )


@BOT.callback_query_handler(func=lambda call: call.data == "cb_anime_remove")
def handle_remove_anime(call):
    BOT.edit_message_text(
        message_id=call.message.message_id,
        chat_id=call.message.chat.id,
        text="Видалення аніме зі списку...",
        reply_markup=menus["remove_menu"]("cb_anime_remove"),
    )


@BOT.callback_query_handler(func=lambda call: call.data == "cb_anime_categories")
def handle_show_anime(call):
    BOT.edit_message_text(
        message_id=call.message.message_id,
        chat_id=call.message.chat.id,
        text="Перегляд списків ...",
        reply_markup=menus["show_menu"]("cb_anime_categories"),
    )


# Handling Select category callbacks
@BOT.callback_query_handler(func=lambda call: "cb_anime_category_seen" in call.data)
def handle_seen_category(call):
    if "cb_anime_add" in call.data:
        BOT.answer_callback_query(call.id, "Відправте назву аніме")
        BOT.register_next_step_handler(
            call.message, handle_anime_title, action="add", category="seen")
        return
    if "cb_anime_remove" in call.data:
        BOT.answer_callback_query(call.id, "Відправте назву аніме")
        BOT.edit_message_text(
            message_id=call.message.message_id,
            chat_id=call.message.chat.id,
            text="\n".join(get_user_anime_by_user_id(
                call.from_user.id, "seen")),
            reply_markup=call.message.reply_markup,
        )
        BOT.register_next_step_handler(
            call.message, handle_anime_title, action="remove", category="seen", call=call)
        return
    if "cb_anime_categories" in call.data:
        BOT.answer_callback_query(call.id, "Перегляд списку переглянутих")
        reply_with_text(call.message, "\n".join(get_user_anime_by_user_id(
            call.from_user.id, "seen")))
        return


@BOT.callback_query_handler(func=lambda call: "cb_anime_category_abandoned" in call.data)
def handle_abandoned_category(call):
    if "cb_anime_add" in call.data:
        BOT.answer_callback_query(call.id, "Відправте назву аніме")
        BOT.register_next_step_handler(
            call.message, handle_anime_title, action="add", category="abandoned")
        return
    if "cb_anime_remove" in call.data:
        BOT.answer_callback_query(call.id, "Відправте назву аніме")
        BOT.edit_message_text(
            message_id=call.message.message_id,
            chat_id=call.message.chat.id,
            text="\n".join(get_user_anime_by_user_id(
                call.from_user.id, "abandoned")),
            reply_markup=call.message.reply_markup,
        )
        BOT.register_next_step_handler(
            call.message, handle_anime_title, action="remove", category="abandoned", call=call)
        return
    if "cb_anime_categories" in call.data:
        BOT.answer_callback_query(call.id, "Перегляд списку покинутих")
        reply_with_text(call.message, "\n".join(get_user_anime_by_user_id(
            call.from_user.id, "abandoned")))
        return


@BOT.callback_query_handler(func=lambda call: "cb_anime_category_liked" in call.data)
def handle_liked_category(call):
    if "cb_anime_add" in call.data:
        BOT.answer_callback_query(call.id, "Відправте назву аніме")
        BOT.register_next_step_handler(
            call.message, handle_anime_title, action="add", category="liked")
        return
    if "cb_anime_remove" in call.data:
        BOT.answer_callback_query(call.id, "Відправте назву аніме")
        BOT.edit_message_text(
            message_id=call.message.message_id,
            chat_id=call.message.chat.id,
            text="\n".join(get_user_anime_by_user_id(
                call.from_user.id, "liked")),
            reply_markup=call.message.reply_markup,
        )
        BOT.register_next_step_handler(
            call.message, handle_anime_title, action="remove", category="liked", call=call)
        return
    if "cb_anime_categories" in call.data:
        BOT.answer_callback_query(call.id, "Перегляд списку улюблених")
        reply_with_text(call.message, "\n".join(get_user_anime_by_user_id(
            call.from_user.id, "liked")))
        return


@BOT.callback_query_handler(func=lambda call: "cb_anime_category_watching" in call.data)
def handle_watching_category(call):
    if "cb_anime_add" in call.data:
        BOT.answer_callback_query(call.id, "Відправте назву аніме")
        BOT.register_next_step_handler(
            call.message, handle_anime_title, action="add", category="watching")
        return
    if "cb_anime_remove" in call.data:
        BOT.answer_callback_query(call.id, "Відправте назву аніме")
        BOT.edit_message_text(
            message_id=call.message.message_id,
            chat_id=call.message.chat.id,
            text="\n".join(get_user_anime_by_user_id(
                call.from_user.id, "watching")),
            reply_markup=call.message.reply_markup,
        )
        BOT.register_next_step_handler(
            call.message, handle_anime_title, action="remove", category="watching", call=call)
        return
    if "cb_anime_categories" in call.data:
        BOT.answer_callback_query(call.id, "Перегляд списку 'Переглядаю'")
        reply_with_text(call.message, "\n".join(get_user_anime_by_user_id(
            call.from_user.id, "watching")))
        return


def handle_anime_title(message, action: str, category: str, call=None):
    if not message.content_type == "text":
        reply_with_text(message, "Введіть назву аніме")
        return
    # split titles by newline
    anime_titles = message.text.split("\n")
    updated = update_user_anime(
        message.from_user.id, anime_titles, action, category)

    match action:
        case "add":
            reply_with_text(message, f"Додання аніме... {anime_titles}")
        case "remove":
            BOT.edit_message_text(
                message_id=call.message.message_id,
                chat_id=call.message.chat.id,
                text="Видалення аніме зі списку...",
                reply_markup=call.message.reply_markup,
            )
            reply_with_text(message, f"Видалення аніме... {anime_titles}" if len(
                list(updated)) else "Аніме не знайдено")


# Handling BACK button callback
@BOT.callback_query_handler(func=lambda call: call.data == "cb_anime_back")
def handle_back_to_main(call):
    BOT.edit_message_text(
        message_id=call.message.message_id,
        chat_id=call.message.chat.id,
        text="Виберіть дію:",
        reply_markup=menus["main_menu"](),
    )
