import speech_recognition as sr
from subprocess import Popen


def ogg_to_wav(ogg_file='./tmp/tmp.voice.ogg'):
    """
    Converting audio .ogg file to .wav for using in recognition
    :param ogg_file: name of file or path to file. Default:
    './tmp/tmp.voice.ogg'
    """
    args = ['ffmpeg', '-i', ogg_file, './tmp/tmp.voice.wav', '-y', '-v', 'quiet']
    process = Popen(args)
    process.wait()

def recognize(file):
    """
    Rocognize the audio file and transfer it into text

    :return: text from audio
    """
    with open('./tmp/tmp.voice.ogg', 'wb') as tmp_voice:
        tmp_voice.write(file)

    ogg_to_wav()

    r = sr.Recognizer()

    with sr.AudioFile('./tmp/tmp.voice.wav') as source:
        audio = r.record(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(
        # audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
        # instead of `r.recognize_google(audio)
        print(r.recognize_google(audio, language='ru-RU'))
        return "Lapis thinks you said:\n" +\
               r.recognize_google(audio, language='ru-RU')
    except sr.UnknownValueError:
        return "Lapis could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Recognize" \
               f" Recognition service; {e}"
