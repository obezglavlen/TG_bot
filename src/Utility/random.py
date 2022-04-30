from random import randint, choice
from src.config import RANDOM_PHRASES
import requests


def get_random_number(a: int, b: int = 0):
    """
    Returning a random number in range a-b, if only 1 argument 0-a

    :param a:
    :param b:
    :return: Random or error
    """
    try:
        return randint(a, b)
    except ValueError:
        return randint(b, a)


def get_random_dick(min=-20, max=10):
    value = get_random_number(min, max)
    return value


def get_random_phrase():
    quote = requests.get("https://animechan.vercel.app/api/random").json()
    print(quote)
    return choice(RANDOM_PHRASES)
