import speech_recognition as sr
from subprocess import Popen


def file2wav(file='./tmp/tmp.file'):
    """
    Converting file to .wav for using in recognition

    :param file: name of file or path to file. Default:
    './tmp/tmp.file'
    """

    args = ['ffmpeg', '-i', file, './tmp/tmp.file.wav', '-y', '-v',
            'quiet']
    process = Popen(args)
    process.wait()


def recognize(file):
    """
    Recognize the audio file and transfer it into text

    :return: text from audio
    """

    with open('./tmp/tmp.file', 'wb') as tmp_file:
        tmp_file.write(file)

    # Convert file
    file2wav()

    r = sr.Recognizer()

    with sr.AudioFile('./tmp/tmp.file.wav') as source:
        audio = r.record(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(
        # audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
        # instead of `r.recognize_google(audio)
        print(r.recognize_google(audio, language='ru-RU'))
        return "Lapis thinks you said:\n" + \
               r.recognize_google(audio, language='ru-RU')
    except sr.UnknownValueError:
        return "Lapis could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Recognize" \
               f" Recognition service; {e}"
