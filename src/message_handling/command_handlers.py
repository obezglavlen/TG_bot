from src.message_handling.utility import reply_with_text, send_msg
from src.config import BOT
import src.Utility.random as rand
import re
from telebot import types
import src.Utility.database as db
from src.Utility.exceptions import TimeoutException, UserNotFoundException
from src.Utility.animelist import menus
from src.message_handling.anime_handlers import anime_search


@BOT.message_handler(commands=["start"])
def send_welcome(message: types.Message):
    """
    Answer welcome message to user, if it wrote "/start" or "/help"
    """
    db.add_new_user(message.from_user)
    reply_with_text(message, "Тринатцать")

    send_contact_button = types.KeyboardButton(
        text="✉ Отправить номер (Опционально)", request_contact=True)
    cancel_button = types.KeyboardButton(text="❌ Отмена")

    def get_markup():
        markup = types.ReplyKeyboardMarkup()
        markup.row_width = 1
        markup.resize_keyboard = True
        markup.add(send_contact_button, cancel_button)

        return markup

    send_msg(message, "Для полной регистрации, отправьте свой контакт",
             reply_markup=get_markup())


@BOT.message_handler(commands=["help", "h"])
def handle_help(message):
    commands: list[types.BotCommand] = BOT.get_my_commands()
    reply_with_text(message, "Список команд:\n" +
                    "\n".join([f"/{command.command} - {command.description}" for command in commands]))


@BOT.message_handler(commands=["search", "s"])
def handle_anime_search(message):
    msg = reply_with_text(
        message, "Відправ мені зображення і я спробую знайти це аніме")
    BOT.register_next_step_handler(msg, anime_search)


@BOT.message_handler(commands=["random", "rand", "r"])
def random_number(message):
    args = re.split(" +", message.text)[1:]

    if len(args) > 2 or len(args) < 1:
        reply_with_text(message, "1 or 2 arguments only")
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


@BOT.message_handler(commands=["randomphrase", "randphrase", "rp"])
def random_phrase(message):
    reply_with_text(message, rand.get_random_phrase())
    return


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


@BOT.message_handler(commands=["anime"])
def hadle_anime_list(message):
    """Handle /anime command and send keyboard with buttons for navigate"""
    answer_message = send_msg(message, "Виберіть дію:")

    markup = menus["main_menu"]

    BOT.edit_message_reply_markup(
        chat_id=message.chat.id, message_id=answer_message.message_id, reply_markup=markup)
