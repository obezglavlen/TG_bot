from random import randint, choice
from src.config import RANDOM_PHRASES
import requests


def get_random_number(a: int, b: int = 0) -> int:
    """
    Returning a random number in range a-b, if only 1 argument 0-a

    Args:
        a (int): First number in range
        b (int, optional): Second number in range
    
    Returns:
        int: Random number
    """
    try:
        return randint(a, b)
    except ValueError:
        return randint(b, a)


def get_random_dick(min=-20, max=10):
    value = get_random_number(min, max)
    return value


def get_random_phrase() -> str:
    """Get random phrase from list

    Returns:
        str: Random phrase
    """
    quote = requests.get("https://animechan.vercel.app/api/random").json()
    return choice(RANDOM_PHRASES)
