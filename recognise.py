#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr


# obtain audio from the microphone
r = sr.Recognizer()

def voice_to_str():
    with sr.Microphone() as source:
        print("Говорите, я слушаю!")
        r.pause_threshold = 1
        audio = r.listen(source)


# recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        result = r.recognize_google(audio,  language='ru-ru')
    except sr.UnknownValueError:
        print("Google Speech Recognition не распознал речь")
        return False
    except sr.RequestError as e:
        print("Не получен ответ от Google Speech Recognition service; {0}".format(e))
        return False

    return result
