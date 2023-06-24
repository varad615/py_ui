import tkinter as tk
import customtkinter
import pyrebase

# Config/Setup
# -------------------------------------------------------------------------------
firebaseConfig = {
    "apiKey":  "AIzaSyB-MLPyckIgRqgBQ4zPrg1wOXsf177Ko5c",
    "authDomain": "info-c1887.firebaseapp.com",
    "projectId": "info-c1887",
    "databaseURL": "https://info-c1887-default-rtdb.firebaseio.com/",
    "storageBucket":  "info-c1887.appspot.com",
    "messagingSenderId": "231830430213",
    "appId": "1:231830430213:web:373acde8a4c07a06bab26c",
    "measurementId": "G-TD52CZE66X"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


def submit_form():
    data = {"Name": name.get(), "email": email.get(), "ph_number": ph.get()}
    # print(data)
    db.child("form").child("data").push(data)


# window
window = customtkinter.CTk()
window.title('Registration Form')
window.geometry('320x300')


# widgets
# title
title_label = customtkinter.CTkLabel(
    master=window, text="Welcome User", fg_color="transparent", font=("Calibri", 24))
title_label.pack()

# Name field
data_frame = customtkinter.CTkFrame(master=window)
entry_int = tk.IntVar()
name = customtkinter.CTkEntry(
    master=data_frame, placeholder_text="Name")
email = customtkinter.CTkEntry(master=data_frame, placeholder_text="Email-Id")
ph = customtkinter.CTkEntry(master=data_frame, placeholder_text="Phone Number")
button = customtkinter.CTkButton(master=data_frame, text="Submit",
                                 command=submit_form)
name.pack(padx=20, pady=10)
email.pack(padx=20, pady=10)
ph.pack(padx=20, pady=10)
button.pack(padx=20, pady=10)
data_frame.pack(pady=10)

# firebase data
# data = {"Name": name.get(), "email": email.get(), "ph_number": ph.get()}

# run
window.mainloop()
