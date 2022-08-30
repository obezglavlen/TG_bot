from ....config import BOT
from ....Utility import database as db
from ....Utility.message_helpers import reply_with_text

@BOT.message_handler(commands=["enable_tts", "disable_tts"])
def toggle_tts(message):
  chat_id = message.chat.id

  chat = db.get_user_by_id(chat_id)

  if message.text == "/enable_tts" and not chat["speechToTextEnable"]:
    db.toggle_chat_tts(chat_id, True)
    reply_with_text(message, "TTS enabled")

  elif message.text == "/disable_tts" and chat["speechToTextEnable"]:
    db.toggle_chat_tts(chat_id, False)
    reply_with_text(message, "TTS disabled")
  else:
    pass
