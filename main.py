import webbrowser
import random

import voice
import recognise
import date

running = 1

def main():
    while running == 1:
        query = recognise.voice_to_str()
        if query:
            query = query.lower()
            print("Вы сказали:", query)
            query = list(query.split(" "))
            if query[0] == "сара" or query[0] == "саров" or query[0] == "zara":
                if any(elem in ["ютубчик", "youеube", "ютуб"] for elem in query):
                    webbrowser.open("https://www.youtube.com/?gl=RU&hl=ru", new=2)
                    voice.say_text("открываю ютубчик")
                elif any(elem in ["привет", "здравствуй", "здорово"] for elem in query):
                    greetings_list = ["превед, медвед", "о, на", "привет"]
                    voice.say_text(random.choice(greetings_list))
                elif any(elem in ["время", "час", "натикало"] for elem in query):
                    time = (date.hours, date.minutes)
                    voice.say_text(time)
                else:
                    voice.say_text("Не знаю такой команды")
        else:
            continue

main()
