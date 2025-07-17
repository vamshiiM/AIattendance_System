import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from tkinter import *
from threading import Thread
import customtkinter
from customtkinter import *
# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # You can adjust the value as needed

# Function to speak the given text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on the time
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

# Function to create a window for "listening" state
def create_listening_window():
    global listening_window
    listening_window = Tk()
    listening_window.title("Listening...")
    listening_window.geometry("300x100")
    label = Label(listening_window, text="Listening...")
    label.pack()
    listening_window.mainloop()

# Function to destroy the "listening" window and create a window for "recognizing" state
def create_recognizing_window():
    # Function to destroy the "listening" window and create a window for "recognizing" state
        global recognizing_window, listening_window
        if listening_window:
             listening_window.destroy()
        recognizing_window = Tk()
        recognizing_window.title("Recognizing...")
        recognizing_window.geometry("300x100")
        label = Label(recognizing_window, text="Recognizing...")
        label.pack()
        recognizing_window.mainloop()






# Function to take voice command and return string output
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Start listening thread
        listening_thread = Thread(target=create_listening_window)
        listening_thread.start()
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        recognizing_thread = Thread(target=create_recognizing_window)
        recognizing_thread.start()
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"



def voice():
   if __name__ == "__main__":
     wish_me()
     while True:
        query = take_command().lower()

        if 'speak' in query:
            speak("FUCK OFF")

        elif 'read' in query:
            speak("the following roll numbers are marked absent")
            # read() function implementation is missing in the provided code

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "vmarri92@gmail.com"
                sendEmail(to, content)  # sendEmail() function implementation is missing in the provided code
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'good boy' in query:
            speak("thank you love you sir")

        elif 'jarvis fetch students' in query:
            speak("here's the list of students")
            # fetch_students() function implementation is missing in the provided code

        elif 'jarvis confirm' in query:
            speak("as you say sir")
            # win() function implementation is missing in the provided code
            create_recognizing_window()

        elif ' jarvis submit' in query:
            speak("AS YOU SAY SIR")
            # sub2() function implementation is missing in the provided code

        elif 'jarvis sleep' in query:
            speak(" okk adios amigo..!")
            break

        else:
            print("No query matched")

def main():
   app=CTk()
   app.geometry("500x500")
   but=CTkButton(app,command=voice)
   but.pack()
   app.mainloop()

def thread():
    thread = Thread(target=main)
    thread.start()


if __name__ == "__main__":
    thread()