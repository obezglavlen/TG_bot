from src.config import DB
import datetime
from src.Utility.exceptions import TimeoutException, UserNotFoundException


def add_new_user(user):
    user = user.to_dict()
    user_id = user["id"]
    username = user["username"]
    user_first_name = user["first_name"]
    user_last_name = user["last_name"]
    user_language_code = user["language_code"]

    if not DB.users.find_one({"_id": user_id}):
        DB.users.insert_one(
            {
                "_id": user_id,
                "user": {
                    "username": username,
                    "first_name": user_first_name,
                    "last_name": user_last_name,
                    "language_code": user_language_code,
                },
            }
        )


def get_user_by_id(user_id):
    user = DB.users.find_one({"_id": user_id})
    if user:
        return user
    else:
        raise UserNotFoundException()


def get_user_by_username(username):
    user = DB.users.find_one({"user.username": username})
    if user:
        return user
    else:
        raise UserNotFoundException()


def get_user_dick(user_id):
    dick = DB.dicks.find_one({"_id": user_id})
    if dick:
        return dick["dick"]
    else:
        return None


def update_user_dick(user_id, dick):
    user_dick = DB.dicks.find_one({"_id": user_id})
    if not user_dick:
        DB.dicks.insert_one(
            {"_id": user_id, "dick": dick, "last_update": datetime.datetime.now()}
        )
    elif user_dick["last_update"] > datetime.datetime.now() - datetime.timedelta(
        hours=1
    ):
        raise TimeoutException(user_dick["last_update"])
    else:
        DB.dicks.update_one(
            {"_id": user_id},
            {"$inc": {"dick": dick}, "$set": {"last_update": datetime.datetime.now()}},
        )

    return get_user_dick(user_id)
