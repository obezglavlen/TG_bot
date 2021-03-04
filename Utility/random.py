from random import random


def get_random_number(*argc):
    """
    Returning a random number in range a-b, if only 1 argument 0-b

    :param argc:
    :return: Random or error
    """
    number_list: list = argc[0]
    range_list: list = []

    if len(number_list) > 2:
        return 'Too many arguments'

    elif len(number_list) == 2:
        for idx, item in enumerate(number_list):
            # Try to convert arguments in integer
            try:
                int(number_list[idx])
            except ValueError:
                return 'It seems like you entered wrong arguments'
            else:
                # Add converted value to range list
                range_list.append(int(number_list[idx]))
        range_list.sort()

    else:
        # Try to convert arguments in integer
        try:
            int(number_list[0])
        except ValueError:
            return 'It seems like you entered wrong arguments'
        else:
            # Add converted value to range list
            range_list.append(int(number_list[0]))

    # Finally returning a random number
    # Formula:
    # rnd(0-1) * (max - min) + min
    if len(range_list) == 1:
        return round(
            random() * range_list[0])
    else:
        return round(
            random() * (range_list[1] - range_list[0]) + range_list[0])
