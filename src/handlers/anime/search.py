import requests

from ...config import BOT, TOKEN
from ...Utility.message_helpers import anime_from_anilist, reply_with_text, reply_with_video
from .filter import filter_anime


def anime_search(message, user_id):
    if message.from_user.id != user_id:
        BOT.register_next_step_handler(message, anime_search, user_id)
        return
    if message.content_type not in ["photo", "animation", "video"]:
        if message.content_type == "text":
            if message.text == "/cancel":
                return
        reply_with_text(message, "Відправте зображення")
        BOT.register_next_step_handler(message, anime_search, user_id)
        return
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
