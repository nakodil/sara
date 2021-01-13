# SAPI 5 from https://github.com/RHVoice/RHVoice/blob/master/doc/en/Binaries.md
# Anna, Arina, Elena, Irina
# Docs https://pyttsx3.readthedocs.io/en/latest/engine.html

import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)

voices = engine.getProperty("voices")  # Список всех доступных голосов

# Задать голос по умолчанию
engine.setProperty("voice", "ru")

# Попробовать установить предпочтительный голос
for voice in voices:
    #print("---")
    #print("Имя:", voice.name)
    #print("ID:", voice.id)
    #print("Язык(и):", voice.languages)
    #print("Пол:", voice.gender)
    #print("Возраст:", voice.age)

    if voice.name == "Anna":
        engine.setProperty("voice", voice.id)

def onStart(name):
   pass

def onWord(name, location, length):
   pass

def onEnd(name, completed):
   pass


# связываем события с функциями
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

    
def say_text(text):
    engine.say(text)  #  собирает реплики в очередь
    engine.runAndWait()  #  воспроизводит очередь 

# engine.save_to_file(text, 'test.mp3')