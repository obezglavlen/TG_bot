from ....config import BOT
from ....Utility import database as db
from ....Utility.message_helpers import reply_with_text

@BOT.message_handler(commands=["enable_stt"])
def enable_tts(message):
  chat_id = message.chat.id

  db.toggle_chat_tts(chat_id, True)
  reply_with_text(message, "STT enabled")

@BOT.message_handler(commands=["disable_stt"])
def disable_tts(message):
  chat_id = message.chat.id

  db.toggle_chat_tts(chat_id, False)
  reply_with_text(message, "STT disabled")