from random import randint


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
