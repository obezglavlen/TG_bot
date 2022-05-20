import re

from ....config import BOT
from ....Utility import random as rand
from ....Utility.message_helpers import reply_with_text


@BOT.message_handler(commands=["random", "rand", "r"])
def random_number(message):
    args = re.split(" +", message.text)[1:]

    if len(args) == 0:
        answers = ["Орел", "Решка"]
        reply_with_text(message, answers[rand.get_random_number(-1, 1)])
        return

    if len(args) > 2:
        reply_with_text(message, "0 or 1 or 2 arguments only")
        return

    try:
        args = list(map(int, args))
    except ValueError:
        reply_with_text(message, "Invalid arguments, only numbers are allowed")
        return

    if len(args) == 1:
        reply_with_text(message, rand.get_random_number(args[0]))
        return

    else:
        reply_with_text(message, rand.get_random_number(args[0], args[1]))
        return
