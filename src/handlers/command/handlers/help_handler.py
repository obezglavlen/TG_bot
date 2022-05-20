from telebot import types

from ....config import BOT
from ....Utility.message_helpers import reply_with_text


@BOT.message_handler(commands=["help", "h"])
def handle_help(message: types.Message):
    commands: list[types.BotCommand] = None
    if message.chat.type == "private":
        commands = BOT.get_my_commands(types.BotCommandScopeAllPrivateChats())
    elif message.chat.type in ["group", "supergroup"]:
        commands = BOT.get_my_commands(types.BotCommandScopeAllGroupChats())
    reply_with_text(message, "Список команд:\n" +
                    "\n".join([f"/{command.command} - {command.description}" for command in commands]))
