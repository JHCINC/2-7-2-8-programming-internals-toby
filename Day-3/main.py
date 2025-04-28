from customtkinter import *
from deep_translator import GoogleTranslator
#import setup

app = CTk()
app.geometry("700x400")
set_appearance_mode("dark")

# List the languages for the translation library

languages = {
    "English": "en",
    "Spanish": "es",
    "Japanese": "ja",
    "French": "fr",
    "German": "de"
}

# Translate

def translate():
    text_to_trans = left_textbox.get("1.0", "end").strip()
    source = left_combo.get()
    target = right_combo.get()
    source_language = languages.get(source)
    target_language = languages.get(target)
    
    trans_text = GoogleTranslator(source=source_language, target=target_language).translate(text_to_trans)
    
    # Allows the translation to be put in
    right_textbox.configure(state="normal")
    right_textbox.delete("1.0", "end")
    right_textbox.insert("1.0", trans_text)
    right_textbox.configure(state="disabled")

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
left_combo.set("English")

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

# Translate Button
translate_button = CTkButton(app, text="Translate", command=translate)
translate_button.grid(row=1, column=0, columnspan=2, pady=10)
app.mainloop()