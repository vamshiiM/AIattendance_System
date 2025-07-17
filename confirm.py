import customtkinter
from customtkinter import*
import tkinter as tk
import mysql.connector

# Establish a connection to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vamshi@51124",
    database="pympr"
)

def display_names():
    # Clear any existing text in the text widget
    box.delete('1.0', tk.END)

    # Get roll numbers entered in the entry field and split them by commas
    roll_nos = tf.get().split(',')

    # Retrieve corresponding names for each roll number from the database
    cursor = mydb.cursor()
    for roll_no in roll_nos:
        roll_no = roll_no.strip()  # Remove leading/trailing whitespace
        cursor.execute("SELECT name FROM s2 WHERE Roll_no = %s", (roll_no,))
        result = cursor.fetchone()
        if result:
            student_name = result[0]
            box.insert(tk.END, f"ROLL NO:  {roll_no},  NAME: {student_name}\n")
        else:
            box.insert(tk.END, f"No data found for Roll No: {roll_no}\n")
    cursor.close()



def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

new = CTk(fg_color="#7360DF")
# new.geometry("700x600")
new.title("THIS IS THE NEW WINDOW")

new.geometry(CenterWindowToDisplay(new, 700, 600, new._get_window_scaling()))
tf = CTkEntry(new)
tf.place(relx=0.1,rely=0.7)
text=tf.get()



box = CTkTextbox(new,width=500,height=300)
box.place(relx=0.15, rely=0.15)


butt = CTkButton(new,command=display_names)
butt.place(relx=0.5, rely=0.8)
new.mainloop()
