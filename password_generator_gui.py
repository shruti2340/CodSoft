# password_generator_advanced_gui.py

import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Password must be at least 4 characters!")
            return
    except ValueError:
        result_label.config(text="Enter a valid number!")
        return

    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        result_label.config(text="Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password:\n{password}")

root = tk.Tk()
root.title("Custom Password Generator")
root.geometry("400x400")

title = tk.Label(root, text="Customizable Password Generator", font=("Arial", 16))
title.pack(pady=10)

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkboxes for character types
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=var_upper).pack()
tk.Checkbutton(root, text="Include Lowercase", variable=var_lower).pack()
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack()
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack()

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()

   