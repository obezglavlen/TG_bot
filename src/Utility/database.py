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

def add_new_chat(chat_id: int) -> dict | None:
  """Add chat to users collection"""
  if not DB.users.find_one({"_id": chat_id}):
    chat = DB.users.insert_one({
      "_id": chat_id,
      "user": None,
      "speechToTextEnable": True
    })
    return chat
  return None

def  toggle_chat_tts(chat_id: int, enabled: bool):
  chat = DB.users.find_one({"_id": chat_id})
  DB.users.update_one({"_id": chat_id},
                      {"$set": {
                        **chat,
                        "speechToTextEnable": enabled
                        }
                        
                      })

def update_user_by_id(user_id: int, user_data: dict) -> dict:
    """Update user data

    Args:
        user_id (int): User id from message.from_user
        user_data (dict): User data to update

    Returns:
        dict: User data after update
    """
    user = DB.users.find_one({"_id": user_id})["user"]
    DB.users.update_one({"_id": user_id}, {
                        "$set": {"user": {**user, **user_data}}}, upsert=True)
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
        DB.dicks.insert_one({"_id": user_id, "dick": dick,
                            "last_update": datetime.datetime.now()})
    elif user_dick["last_update"] > datetime.datetime.now() - datetime.timedelta(hours=1):
        raise TimeoutException(user_dick["last_update"])
    else:
        DB.dicks.update_one(
            {"_id": user_id},
            {"$inc": {"dick": dick}, "$set": {
                "last_update": datetime.datetime.now()}},
        )

    return get_user_dick(user_id)


def get_user_anime_by_user_id(user_id: int, category: str) -> list:
    """Get user anime data by user id

    Args:
        user_id (int): User id from message.from_user

    Returns:
        list: User anime
    """
    user_anime = DB.anime.find_one({"_id": user_id})
    if not user_anime:
        return []
    match category:
        case "seen":
            if "anime_seen" in user_anime and len(user_anime["anime_seen"]):
                animes: list = user_anime["anime_seen"]
                animes.sort()
                return animes
            else:
                return []
        case "watching":
            if "anime_watching" in user_anime and len(user_anime["anime_watching"]):
                animes = user_anime["anime_watching"]
                animes.sort()
                return animes
            else:
                return []
        case "liked":
            if "anime_liked" in user_anime and len(user_anime["anime_liked"]):
                animes = user_anime["anime_liked"]
                animes.sort()
                return animes
            else:
                return []
        case "future":
            if "anime_future" in user_anime and len(user_anime["anime_future"]):
                animes = user_anime["anime_future"]
                animes.sort()
                return animes
            else:
                return []


def setup_user_anime(user_id: int):
    """Setup user anime

    Args:
        user_id (int): User id from message.from_user
    """
    user_anime = DB.anime.find_one({"_id": user_id})
    if not user_anime:
        DB.anime.insert_one({"_id": user_id,
                             "anime_seen": [],
                             "anime_watching": [],
                             "anime_liked": [],
                             "anime_future": []
                             })


def update_user_anime(user_id: int, animes: list, action: str, category: str) -> list:
    """Update user anime data

    Args:
        user_id (int): User id from message.from_user
        anime (str): List of anime to add
        action (str): Action to perform

    Returns:
        list: User anime after update
    """
    user_anime = DB.anime.find_one({"_id": user_id})
    updated = []
    if not user_anime:
        match action:
            case "add":
                DB.anime.insert_one(
                    {"_id": user_id})
                DB.anime.update_one(
                    {"_id": user_id},
                    {"$addToSet": {f"anime_{category}": {"$each": animes}}}
                )
                return animes
            case "remove":
                return []

    else:
        old_animes = get_user_anime_by_user_id(user_id, category)
        match action:
            case "add":
                # make a list with items that are in animes but not in old_animes
                new_animes = [
                    item for item in animes if item not in old_animes]

                DB.anime.update_one(
                    {"_id": user_id}, {"$addToSet": {f"anime_{category}": {"$each": animes}}}, upsert=True
                )
                return new_animes
            case "remove":
                removed_animes = [
                    item for item in animes if item in old_animes]

                DB.anime.update_one(
                    {"_id": user_id}, {"$pull": {f"anime_{category}": {"$in": animes}}}, upsert=True
                )

                return removed_animes
