from src.message_handling.utility import (
    reply_with_text,
    reply_with_video,
    anime_from_anilist,
)
import requests
from src.config import BOT
import os
import telebot


def filter_anime(anime: list):
    """
    Filter anime from anilist
    """
    used_anilists = []
    filtered_results = []
    for result in anime:
        if result["anilist"] not in used_anilists:
            used_anilists.append(result["anilist"])
            if result["similarity"] > 0.9:
                filtered_results.append(result)

    return filtered_results


@BOT.message_handler(
    func=lambda message: True,
    content_types=["photo", "animation", "video"],
)
def anime_pic(message):
    if message.caption == "/anime":
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
        file_url = f"https://api.telegram.org/file/bot{os.environ.get('TELEGRAM_TOKEN')}/{file_path}"
        api_url = f"https://api.trace.moe/search?{'&'.join([f'uid=tg{message.from_user.id}', f'url={file_url}', 'cutBorders=1'])}"
        search_result = None
        try:
            search_result = requests.get(api_url)
        except Exception:
            reply_with_text(message, "trace.moe API error, please try again later.")
            return

        if not search_result:
            reply_with_text(message, "trace.moe API error, please try again later.")
            return
        if search_result.status_code in [502, 503, 504]:
            reply_with_text(
                message, "trace.moe server is busy, please try again later."
            )
            return
        if search_result.status_code in [402, 429]:
            reply_with_text(
                message, "You exceeded the search limit, please try again later"
            )
            return
        if search_result.status_code >= 400:
            reply_with_text(message, "trace.moe API error, please try again later.")
            return

        search_result = search_result.json()

        if search_result["error"]:
            reply_with_text(message, "trace.moe API error, please try again later.")
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
            filename = result["filename"]
            video = result["video"]

            anime = None
            try:
                anime = anime_from_anilist(anilist)
            except Exception:
                reply_with_text(message, "Anilist API error, please try again later.")
                return

            if not anime:
                reply_with_text(message, "Anilist API error, please try again later.")
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

            reply_with_text(message, reply_message) if anime[
                "isAdult"
            ] else reply_with_video(message, video, reply_message)
        return
