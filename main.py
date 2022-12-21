import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_auto import *
from News import *
import randfacts
from jokes import *
from weather import *
import datetime

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 138)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return ("morning")
    elif hour >= 12 and hour < 16:
        return ("afternoon")
    else:
        return ("evening")

today_date = datetime.datetime.now()
r = sr.Recognizer()

speak("hello sir, good " + wishme() + ", I'm SIRI, your voice assistant.")
speak("today is" + today_date.strftime("%d") + " of " + today_date.strftime("%B") + ", And its currently " +  (today_date.strftime("%I")) +  (today_date.strftime("%H")) + (today_date.strftime("%p")))
speak("Temperature in new cairo is " + str(temp()) + " degree celcius " + " and with " + str(des()))
speak("Let me start by asking, How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am also having a good day sir")
speak("what can i do for you??")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
print(text2)

if "search" in text2:
    speak("sure sir, what do you want to search for? ")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("sure, now i will search for {} in wikipedia".format(infor))
    print("sure, now i will search for {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

speak("now, what can i do for you??")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
print(text2)

if "play" and "video" in text2:
    speak("you want me to play which video??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        print("Playing {} on youtube".format(vid))
        speak("Playing {} on youtube".format(vid))

        assist = music()
        assist.play(vid)

speak("now, how can i help you??")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
print(text2)

if "news" in text2:
    print("Sure sir, Now I will read news for you.")
    speak("Sure sir, Now I will read news for you.")

    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])



if "fact" in text2:
    speak("Sure sir,")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, " + x)

speak("now, how can i help you??")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
print(text2)

if "joke" in text2:
    speak("sure sir, get ready for some chuckles")
    ar = joke()
    print(ar[0])
    speak(ar[0])
    print(ar[1])
    speak(ar[1])

speak("now, what can i do for you??")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
print(text2)

if "bye" and "exit" in text2:
    print("ok, bye")
    speak("ok, bye")
