import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print("Candy:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.7)
        audio = r.listen(source, timeout=5, phrase_time_limit=6)

    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Network problem")
        return ""

speak("Candy assistant is online")

while True:
    text = listen()

    # WAKE WORD MODE
    if "candy" in text:
        speak("Yes master, how can I help you")

        # ACTIVE SESSION MODE
        while True:
            command = listen()

            if command == "":
                speak("I did not hear anything")
                continue

            # TIME
            if "time" in command:
                now = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {now}")

            # DATE
            elif "date" in command:
                today = datetime.datetime.now().strftime("%B %d, %Y")
                speak(f"Today's date is {today}")

            # YOUTUBE
            elif "youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")

            # SLEEP MODE
            elif "stop" in command or "sleep" in command:
                speak("Going to sleep master")
                break

            else:
                speak("Sorry master, I don't understand that")
