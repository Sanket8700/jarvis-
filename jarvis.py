from email.mime import audio
from logging import exception
from multiprocessing import Condition
from pickle import TRUE
from urllib import request
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import wikipedia
import pyjokes
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyautogui
import instaloader
from bs4 import BeautifulSoup
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
# text to speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# audio to text


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"user said: {command }")

    except Exception as e:
        speak("say that again please...")
        return "none"
    command = command.lower()
    return command

# to send email


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('sanketmathur050@gmail,com', 'sanket@2002')
    server.sendmail('sanketmathur050@gmail.com', to, content)
    server.close()


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning... its{tt}")
        print(f"good morning... its {tt}")

    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon...  its {tt}")
        print(f"good afternoon...  its {tt}")

    else:
        speak(f"good evening... its {tt}")
        print(f"good evening... its {tt}")
    speak("i am jarvis sir , please give me command ")
    print("i am jarvis sir , please give me command ")


def taskexecution():
    wish()
    while True:

        # if 1:
        command = take_command()
        if "open notepad" in command:
            speak("opening notepad sir, please wait")
            print("opening notepad sir, please wait")
            npath = "C:\\windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open cmd' in command:
            speak("opening cmd  sir, please wait")
            print("opening cmd  sir, please wait")
            npath = "C:\\windows\\system32\\cmd.exe"
            os.startfile(npath)

        elif "open camera" in command:
            speak("opening camera sir , please wait")
            print("opening camera sir , please wait")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "music" in command:
            speak("playing music sir , please wait ")
            print("playing music sir , please wait")
            music_dir = "C:\\windows\\system32"
            songs = os.listdir(music_dir)
            #rd= random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif " ip address " in command:
            speak("fetching ip address sir , wait few second")
            print("fetching ip address sir , wait few second")
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
            print(ip)

        elif 'play' in command:
            song = command.replace('play',  '')
            speak('playing.....' + song)
            print("playing...... " + song)
            kit.playonyt(song)

        elif 'wikipedia' in command:
            speak("fetching information , it may take some time ")
            print("fetching information , it may take some time ")
            person = command.replace('wikipedia',  '')
            info = wikipedia.summary(person, 5)
            print(info)
            speak(info)

        elif"open google" in command:
            speak("sir ,what should i search on google")
            print("sir , what should i search on google")
            cm = take_command()
            webbrowser.open(f"{cm}")

        elif "open instagram" in command:
            speak("opening instagram , sir please wait")
            print("opening instagram, sir please wait")
            webbrowser.open("www.instagram.com")

        elif "open facebook" in command:
            speak("opening facebook , sir please wait")
            print("opening facebook , sir please wait")
            webbrowser.open("www.facebook.com")

        elif "open twitter" in command:
            speak("opening twitter , sir please wait")
            print("opening twitter , sir please wait")
            webbrowser.open("www.twitter.com")

        elif"open stack overflow" in command:
            speak("opening stack overfolw , sir please wait")
            print("opening stack overfolw , sir please wait")
            webbrowser.open("www.stackoverflow.com")
        elif "open whatsapp" in command:
            speak("opening whatsapp , sir please wait")
            print("opening whatsapp , sir please wait")
            webbrowser.open("https://web.whatsapp.com/")

        elif "send massage" in command:
            kit.sendwhatmsg("+919897567975", "hello this is sanket", 11, 32)
            speak("massage has been sent")
            print("massage has been sent")

        elif"email to lavish" in command:
            try:
                speak("what should i say")
                content = take_command()
                to = "chawlalavish0073@gmail.com"
                sendEmail(to, content)
                speak('email has been sent to lavish')
                print('enail has been sent to lavish')

            except Exception as e:
                print(e)
                speak("sorry sir , i am not able to sent this mail")
                print("sorry sir , i am not able to sent this mail")

        elif "you can sleep " in command:
            speak("thanks  for using jarvis sir, have a good day")
            print("thanks for using jarvisn sir, have a good day")
            break

        # to close application

        elif "close notepad" in command:
            speak("okey sir, closing notepad")
            os.system("TASKKILL  / im notepade.exe /f /t")

        elif "close cmd " in command:
            speak("okey sir, closing  cmd ")
            os.system("TASKKILL /f / im cmd.exe")

        # to set alarm
        # elif "alarm" in command:
        #     speak("sir, please tell me the time to set the alarm ")
        #     at = take_command()
        #     at = at.replace("set alarm to ", "")
        #     at = at.replace(".", "")
        #     at = at.upper()
        #     import myalarm
        #     myalarm.alarm(at)

        # to shutdown the system
        elif "shutdown" in command:
            os.system("shutdown /s ")

        # to rstart the system
        elif " restart the system" in command:
            os. system("shutdown /r")

        elif" sleep the system" in command:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # to switch the window
        elif" change window" in command:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        # to check insta profile

        elif "instagram profile" in command or "profiles on instagram" in command:
            speak("sir please enter the user name correctly.")
            print("sir please enter thge user name correctly ")
            name = input("enter the user name : ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            print(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir, would you like to download the profile picture of this account")
            print("sir, would you like to download the profile picture of this account")
            Condition = take_command()
            if "yes" in Condition:
                mod = instaloader.instaloader()
                mod.download_profile(name, profile_picture_only=True)
                speak(
                    "i am done sir . profile picture is downloaded in our main folder ")
                print("i am done sir . profile picture is downloaded in our main folder")
            else:
                pass

        elif "take screenshot" in command or "take a screnshot" in command:
            speak("sir , please tell me the name of this screenshot file ")
            print("sir, please tell me the name of this screenshot file ")
            name = take_command()
            speak("please hold the screen for few second , i am taking screenshot")
            print("please hold the screen for few second  , iam taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir , the screenshot is saved in our main folder.")

        elif"hello jarvis" in command:
            speak("hello sir, may i help you ")
            print("hello sir , may i help you")

        elif"how are you" in command:
            speak("i am good sir, what about you")
            print("i am good sir , what about you")

        elif"what are you doing" in command :
            speak("i am trying to help you")
            print("i am trying to help you")
        

        # temprature checking
        elif"temperature" in command:
            search = "temperatur in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = request.urlopen(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        speak("sir, do you have any other work")
        print("sir , do you have any  other work")


if __name__ == "__main__":
    while True:
        permission = take_command()
        if "wake up" in permission:
            taskexecution()
        #turning off
        elif"goodbye" in permission:
            speak("thanks for using jarvis,sir ")
            print("thanks for using jarvis,sir ")
            sys.exit()
