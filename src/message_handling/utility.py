from telebot import types
from src.config import BOT
import requests


def reply_with_sticker(message: types.Message, sticker_id: str) -> None:
    """
    Overwrite method to reply on message with sticker

    :param message: message object from bot
    :param sticker_id: sticker id to send
    """
    BOT.send_sticker(message.chat.id, sticker_id, reply_to_message_id=message.message_id)


def reply_with_text(message: types.Message, text: str, markdown: bool = False) -> None:
    """Overwrite method to reply on message with text

    Args:
        message (telebot.types.Message): message object from bot
        text (str): text to reply
        markdown (bool, optional): if True, text will be sent as markdown
    """

    BOT.reply_to(message, text, parse_mode="Markdown" if markdown else None)


def reply_with_video(message: types.Message, video: str, text: str) -> None:
    """Overwrite method to reply on message with video

    Args:
        message (telebot.types.Message): message object from bot
        video (str): video url
        text (str): text to reply
    """
    BOT.send_video(
        chat_id=message.chat.id,
        reply_to_message_id=message.message_id,
        video=video,
        caption=text,
    )


def anime_from_anilist(anilist: int) -> dict:
    """Get anime from anilist api

    Args:
        anilist (int): anilist id

    Returns:
        dict: anime data
    """

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
    if not response:
        raise Exception("Error: No response")

    response = response.json()

    return response["data"]["Media"]
