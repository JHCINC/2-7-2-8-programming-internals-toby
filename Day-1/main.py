from customtkinter import *
from deep_translator import GoogleTranslator
#import setup

app = CTk()
app.geometry("700x400")
set_appearance_mode("dark")

# Functions

def translate():
    pass

def language():
    pass


# Create frames for left and right sides
left_frame = CTkFrame(app)
left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

right_frame = CTkFrame(app)
right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Grid weights
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# Left side components
left_combo = CTkComboBox(
    left_frame,
    values=["English", "Spanish", "Japanese", "French", "German"],
    state="readonly")
left_combo.pack(pady=10, padx=10)

left_textbox = CTkTextbox(left_frame, width=300, height=300)
left_textbox.pack(pady=10, padx=10)


# Right side components
right_combo = CTkComboBox(
    right_frame,
    values=["English", "Spanish", "Japanese", "French", "German"],
    state="readonly")
right_combo.pack(pady=10, padx=10)

right_textbox = CTkTextbox(right_frame, width=300, height=300, state="disabled")
right_textbox.pack(pady=10, padx=10)

app.mainloop()