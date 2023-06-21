import tkinter as tk
from tkinter import ttk
import customtkinter


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_sting.set(km_output)


# window
window = customtkinter.CTk()
window.title('Convertor')
window.geometry('320x150')

# widgets
# title
title_label = customtkinter.CTkLabel(
    master=window, text="Miles to Kilometer", fg_color="transparent", font=("Calibri", 24))
title_label.pack()

# input field
input_frame = customtkinter.CTkFrame(master=window)
entry_int = tk.IntVar()
entry = customtkinter.CTkEntry(master=input_frame, textvariable=entry_int)
button = customtkinter.CTkButton(master=input_frame, text="Convert",
                                 command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_sting = tk.StringVar()
output_label = customtkinter.CTkLabel(master=window,
                                      font=("Calibri", 24), textvariable=output_sting, fg_color="transparent",)
output_label.pack(pady=5)

# run
window.mainloop()
