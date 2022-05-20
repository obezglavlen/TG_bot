from ....config import BOT
from ...anime.search import anime_search
from ....Utility.message_helpers import reply_with_text


@BOT.message_handler(commands=["search", "s"])
def handle_anime_search(message):
    msg = reply_with_text(
        message, "Відправ мені зображення і я спробую знайти це аніме")
    BOT.register_next_step_handler(msg, anime_search, message.from_user.id)
