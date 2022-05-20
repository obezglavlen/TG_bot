from ....config import BOT
from ....Utility.speech_recognize import recognize
from ....Utility.message_helpers import reply_with_text


@BOT.message_handler(
    func=lambda message: True,
    content_types=["video_note", "voice", "audio"],
)
def audio_recognize(message):
    """
    Converting message document to text. Need "ffmpeg". Install it before
    using. Else comment this handler

    :param message: message object from bot
    """
    # Get content type as string from message object
    content_type = message.content_type

    # Get file from bot with it info data
    file_id = getattr(message, content_type).file_id
    file_info = BOT.get_file(file_id)
    downloaded_file = BOT.download_file(file_info.file_path)

    # Reply with returned str
    reply_with_text(message, recognize(downloaded_file))
