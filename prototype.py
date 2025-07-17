import pyttsx3
import speech_recognition as sr
import datetime
import threading
import tkinter as tk
import wikipedia
import webbrowser

listening_window = None
stop_listening_flag = False
stop_recognizing_flag=False
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I assist you today?")

def create_listening_window():
    global listening_window, stop_listening_flag
    listening_window = tk.Tk()
    listening_window.title("Listening...")
    listening_window.geometry("300x100")
    button = tk.Button(listening_window, text="Stop Listening", command=on_click)
    button.pack()
    listening_window.mainloop()

def create_recognizing_window():
    global recognizing_window
    recognizing_window = tk.Tk()
    recognizing_window.title("Recognizing...")
    recognizing_window.geometry("300x100")
    recognizing_window.mainloop()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        global stop_recognizing_flag
        stop_recognizing_flag = True

        threading.Thread(target=create_listening_window).start()
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        global stop_listening_flag
        stop_listening_flag = True
        # listening_window.destroy()
        threading.Thread(target=create_recognizing_window).start()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print(e)
        print("Say that again, please...")
        return "None"

def on_click():
    global stop_listening_flag
    stop_listening_flag = True

if __name__ == "__main__":
    wish_me()
    query = take_command().lower()
