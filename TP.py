import tkinter as tk
import speech_recognition as sr
import threading
from threading import Thread
import pyttsx3
import datetime
import webbrowser
import tkinter as tk
from tkinter import Label
import customtkinter
from customtkinter import *
# Initialize the recognizer


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
    listening_window = tk.Tk()
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
        recognizing_window = tk.Tk()
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
        speak("I'm sorry Say that again please...")
        return "None"

def c():
    threading.Thread(target=take_command).start()




def voice():
    wish_me()
    while True:
        query = take_command().lower()

        if 'speak' in query:
            speak("FUCK OFF")

        elif 'read' in query:
            speak("the following roll numbers are marked absent")
            #read()

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
            fetch_students()

        elif 'jarvis confirm' in query:
            speak("as you say sir")
            # win() function implementation is missing in the provided code
            create_recognizing_window()

        elif ' jarvis submit' in query:
            speak("AS YOU SAY SIR")
            # sub2() function implementation is missing in the provided code
        elif 'jarvis initiate roll call' in query:
            speak("Initiating roll call")
            create_gui()


        elif 'jarvis sleep' in query:
            speak(" okk adios amigo..!")
            break

        else:
            print("No query matched")


def start_listening():
    threading.Thread(target=voice).start()

def listen(entry):
    threading.Thread(target=speech_to_text, args=(entry,)).start()

def speech_to_text(entry):
    recognizer = sr.Recognizer()
    speak("Please SPEAK ONE ROLL NUMBER AT A TIME")
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            listening_thread = Thread(target=create_listening_window)
            listening_thread.start()
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            recognizing_thread = Thread(target=create_recognizing_window)
            recognizing_thread.start()
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            speak(text)
            if text.lower() == "stop" or text.lower == "successful":
                speak("closing the process")
                break
            else:
                # Extract roll numbers from recognized text
                roll_numbers = extract_roll_numbers(text)
                if roll_numbers:
                    # Insert roll numbers into the entry field separated by commas
                    for roll_number in roll_numbers:
                        entry.insert(tk.END, roll_number + ", ")
                        entry.update()
                        speak("ROLL NUMBER ADDED")
                # Update the GUI to reflect the changes
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            speak("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak(f"Could not request results from Google Speech Recognition service; {e}")




# Function to extract roll numbers from the recognized text
def extract_roll_numbers(text):
    roll_numbers = []
    for word in text.split():
        if word.isdigit():
            roll_numbers.append(word)
    return roll_numbers




def listen(entry):
    threading.Thread(target=speech_to_text(entry)).start()

# Main function to create the GUI
def create_gui():
    root = CTk()
    root.title("Speech to Roll Numbers")
    root.geometry("500x500")

    entry = CTkEntry(root, width=400,height=20)
    entry.pack(pady=10)

    # Function to add a comma after every number inputted
    def add_comma(event):
        current_text = entry.get()
        if current_text.endswith(" ") or current_text.endswith(","):
            entry.insert(tk.END, "")
        else:
            entry.insert(tk.END, ", ")

    # Bind the add_comma function to the Key event of the entry field
    entry.bind("<Key>", add_comma)



    button = CTkButton(root,height=20,width=100, text="Start Listening", command=lambda: listen(entry))
    button.place(relx=0.5,rely=0.5)
    button1 = CTkButton(root, height=20, width=100, text="Start Listening", command=input)
    button1.place(relx=0.5, rely=0.6)


    root.mainloop()

def input():
  root = CTk()
  e1=entry.get().split(",")
  entry.insert(0, ', '.join(e1))
  entry.update()
  root.destroy()

app=customtkinter.CTk()
app.geometry("500x500")
butt=CTkButton(app,text="VOICE",command=voice)
butt.pack()
entry = CTkEntry(app, width=400, height=20)
entry.pack(pady=10)
app.mainloop()



# Run the GUI
if __name__ == "__main__":
    app.mainloop()
