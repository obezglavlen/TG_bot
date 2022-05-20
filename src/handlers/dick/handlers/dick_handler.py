import re

from ....config import BOT
from ....Utility import database as db
from ....Utility import random as rand
from ....Utility.exceptions import TimeoutException, UserNotFoundException
from ....Utility.message_helpers import reply_with_text


@BOT.message_handler(commands=["dick"])
def dick(message):
    """
    Simple random game, for fun
    """
    args = re.split(" +", message.text)[1:]

    if len(args) >= 1:
        if args[0].startswith("@"):
            entity = args[0][1:]
            try:
                user = db.get_user_by_username(entity)
            except UserNotFoundException:
                reply_with_text(message, "User not found")
                return
            user_dick = db.get_user_dick(user["_id"])
            if user_dick:
                reply_with_text(
                    message, f"У этого {entity} елдыга {user_dick} миллиметров")
                return
            else:
                reply_with_text(message, f"У этого {entity} нет елдыга")
                return
    else:
        dick_change = rand.get_random_dick()
        try:
            user_dick = db.update_user_dick(message.from_user.id, dick_change)

            if dick_change > 0:
                reply_with_text(
                    message,
                    f"Конгратулатион, йор дик вырас на {dick_change} милиметров.\nТеперь твой дик {user_dick} милиметров.",
                )
            else:
                reply_with_text(
                    message,
                    f"Собол, йор дик упал на {dick_change} милиметров.\nТеперь твой дик {user_dick} милиметров.",
                )
            return
        except (TimeoutException, UserNotFoundException) as e:
            reply_with_text(message, e.message)
            return
