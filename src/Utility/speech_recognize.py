import speech_recognition as sr
from subprocess import Popen

path = "./tmp/tmp.file"
path_wav = "./tmp/tmp.file.wav"


def file2wav(in_file: str = path, out_file: str = path_wav):
    """Converting file to .wav for using in recognition

    Args:
        in_file (str, optional): name of file or path to file. Default: "../tmp/tmp.file"
        out_file (str, optional): name of file or path to file. Default: "../tmp/tmp.file.wav"
    """

    args = ["ffmpeg", "-i", in_file, out_file, "-y", "-v", "quiet"]
    process = Popen(args)
    process.wait()


def recognize(file):
    """Recognize the audio file and transfer it into text

    Args:
        file (str): name of file or path to file. Default: "../tmp/tmp.file.wav"
    Returns:
        str: text from audio
    """

    with open(path, "wb") as tmp_file:
        tmp_file.write(file)

    # Convert file
    file2wav()

    r = sr.Recognizer()

    with sr.AudioFile(path_wav) as source:
        audio = r.record(source)

    try:
        # for testing purposes, we"re just using the default API key
        # to use another API key, use `r.recognize_google(
        # audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
        # instead of `r.recognize_google(audio)
        text = r.recognize_google(audio, language="ru-RU")
        print(text)
        return text
    except sr.UnknownValueError:
        return "Lapis could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Recognize\nError: {e}"
