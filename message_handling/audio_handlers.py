


# Просто обознач в голове файла нахуй 3 строки отступи и комментом там
# напиши "хуйовые комменты, переделай"




from message_handling.utility import reply_with_text
from config import BOT
from speech_recognize import recognize


@BOT.message_handler(func=lambda message: True, content_types=[
    'video_note', 'video', 'voice'])
def audio_recognize(message):
    """
    Info

    :param message: message object from bot
    """

    # COMMENTS FUCK ITSELF REWORK


    # Получаем тип сообщения ('video_note', 'video', 'voice') из св-в message
    content_type = message.content_type

    # Получаем id файла из сообщения
    file_id = getattr(message, content_type).file_id

    # Получаем информацию о файле, по его id
    file_info = BOT.get_file(file_id)

    # Получаем файл, по его пути
    downloaded_file = BOT.download_file(file_info.file_path)

    # ф-я распознования речи
    reply_with_text(message, recognize(downloaded_file))
