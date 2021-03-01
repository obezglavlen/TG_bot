import speech_recognition as sr
from subprocess import Popen


def ogg_to_wav(ogg_file='./tmp/tmp.voice.ogg'):
    args = ['ffmpeg', '-i', ogg_file, './tmp/tmp.voice.wav']
    process = Popen(args)
    process.wait()

def recognize(file):
    """

    :return: speech to text
    """
    with open('./tmp/tmp.voice.ogg', 'wb') as tmp_voice:
        tmp_voice.write(file)

    ogg_to_wav()

    # r = sr.Recognizer()
    #
    # with sr.AudioFile('.tmp/tmp.voice.wav') as source:
    #     audio = r.record(source)
    #
    # try:
    #     # for testing purposes, we're just using the default API key
    #     # to use another API key, use `r.recognize_google(
    #     # audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    #     # instead of `r.recognize_google(audio)
    #     print(
    #         "Google Speech Recognition thinks you said " + r.recognize_google(
    #             audio))
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand audio")
    # except sr.RequestError as e:
    #     print(
    #         "Could not request results from Google Speech Recognition service; {0}".format(
    #             e))
