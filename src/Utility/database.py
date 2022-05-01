from src.config import DB
import datetime
from src.Utility.exceptions import TimeoutException, UserNotFoundException
from telebot import types


def add_new_user(user: types.User) -> dict | None:
    """Add new user to database

    Args:
        user (telebot.types.User): User data
    """
    user = user.to_dict()
    user_id = user["id"]
    username = user["username"]
    user_first_name = user["first_name"]
    user_last_name = user["last_name"]
    user_language_code = user["language_code"]
    user_number = None

    if not DB.users.find_one({"_id": user_id}):
        user = DB.users.insert_one(
            {
                "_id": user_id,
                "user": {
                    "username": username,
                    "first_name": user_first_name,
                    "last_name": user_last_name,
                    "language_code": user_language_code,
                    "number": user_number,
                },
            }
        )
        return user
    return None


def update_user_by_id(user_id: int, user_data: dict) -> dict:
    """Update user data

    Args:
        user_id (int): User id from message.from_user
        user_data (dict): User data to update

    Returns:
        dict: User data after update
    """
    user = DB.users.find_one({"_id": user_id})["user"]
    DB.users.update_one({"_id": user_id}, {"$set": {"user": {**user, **user_data}}}, upsert=True)
    return get_user_by_id(user_id)


def get_user_by_id(user_id: int) -> dict:
    """Get user data by user id

    Args:
        user_id (int): User id from message.from_user

    Raises:
        UserNotFoundException: If user is not in database

    Returns:
        dict: User data
    """
    user = DB.users.find_one({"_id": user_id})
    if user:
        return user
    else:
        raise UserNotFoundException()


def get_user_by_username(username: str) -> dict:
    """Get user data by username

    Args:
        username (str): Username from message.from_user

    Raises:
        UserNotFoundException: If user is not in database

    Returns:
        dict: User data
    """
    user = DB.users.find_one({"user.username": username})
    if user:
        return user
    else:
        raise UserNotFoundException()


def get_user_dick(user_id: int) -> int | None:
    """Get user dick

    Args:
        user_id (int): User id from message.from_user

    Returns:
        int: User dick
        None: If user is not in database
    """
    dick = DB.dicks.find_one({"_id": user_id})
    if dick:
        return dick["dick"]
    else:
        return None


def update_user_dick(user_id, dick) -> int:
    """Update user dick data

    Args:
        user_id (int): User id from message.from_user
        dick (int): Value to increase

    Raises:
        TimeoutException: If last update was less than 1 hour ago

    Returns:
        int: User dick after update
    """
    user_dick = DB.dicks.find_one({"_id": user_id})
    if not user_dick:
        DB.dicks.insert_one({"_id": user_id, "dick": dick, "last_update": datetime.datetime.now()})
    elif user_dick["last_update"] > datetime.datetime.now() - datetime.timedelta(hours=1):
        raise TimeoutException(user_dick["last_update"])
    else:
        DB.dicks.update_one(
            {"_id": user_id},
            {"$inc": {"dick": dick}, "$set": {"last_update": datetime.datetime.now()}},
        )

    return get_user_dick(user_id)
