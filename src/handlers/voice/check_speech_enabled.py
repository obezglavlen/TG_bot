from ...Utility import database as db

def check_speech_enabled(chat_id: int):
  chat = db.get_user_by_id(chat_id)

  if chat["speechToTextEnable"]: return True
  else: return False
