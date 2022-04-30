from telebot import types
from src.config import BOT
import requests

# Создал функцию, чтобы можно было прикрепить к стикеру ответ


def reply_with_sticker(message: types.Message, sticker_id: str):
    """
    Overwrite method to reply on message with sticker

    :param message: message object from bot
    :param sticker_id: sticker id to send
    """
    BOT.send_sticker(
        message.chat.id, sticker_id, reply_to_message_id=message.message_id
    )


# Решил уже и тут сделать отдельную функцию, ибо чтобы было в едином стиле
def reply_with_text(message: types.Message, text: str):
    """
    Overwrite method to reply on message with text

    :param message: message object from bot
    :param text: text to answer
    """
    BOT.reply_to(message, text)


def reply_with_markdown(message: types.Message, text: str):
    """
    Overwrite method to reply on message with text

    :param message: message object from bot
    :param text: text to answer
    """
    BOT.reply_to(message, text, parse_mode="Markdown")


def reply_with_video(message: types.Message, video: str, text: str):
    """
    Overwrite method to reply on message with video

    :param message: message object from bot
    :param video: video to answer
    :param caption: caption to answer
    """
    BOT.send_video(
        chat_id=message.chat.id,
        reply_to_message_id=message.message_id,
        video=video,
        caption=text,
    )


def anime_from_anilist(anilist: int):
    query = """
        query ($id: Int) { # Define which variables will be used in the query (id)
            Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
                title {
                romaji
                english
                native
                }
                isAdult
            }
        }
    """

    variables = {"id": anilist}

    url = "https://graphql.anilist.co"

    response = requests.post(url, json={"query": query, "variables": variables})

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")

    response = response.json()

    return response["data"]["Media"]
