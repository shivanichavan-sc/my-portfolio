import tkinter as tk
import string
from tkinter import ttk
import random

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x300+500+200")
#
# ttk.Label(root,text="Password Length:").pack(pady= 5)
#
# use_upper = tk.BooleanVar(value=True)
# use_lower = tk.BooleanVar(value=True)
# use_digits = tk.BooleanVar(value=True)
# use_symbols = tk.BooleanVar(value=False)
#
# ttk.Checkbutton(root,text="Include Uppercase", variable=use_upper).pack()
# ttk.Checkbutton(root,text="Include Lowercase", variable=use_lower).pack()
# ttk.Checkbutton(root, text="Include Digits", variable=use_digits).pack()
# ttk.Checkbutton(root, text="Include Symbols", variable= use_symbols).pack()
#
# length_var = tk.IntVar(value = 12)
# ttk.Spinbox(root, from_=4, to = 64, textvariable=length_var).pack()
#
# def generate_password():
#     chars = ""
#     if use_upper.get():
#         chars += string.ascii_uppercase
#     if use_lower.get():
#         chars += string.ascii_lowercase
#     if use_digits.get():
#         chars += string.digits
#     if use_symbols.get():
#         chars += string.punctuation
#
#     if not chars:
#         password_var.set("Select at least one option.").pack()
#         return
#
#     length = length_var.get()
#     password = "".join(random.choice(chars) for _ in range(length))
#     password_var.set(password)
#
# password_var = tk.StringVar()
#
# result_entry = ttk.Entry(root, textvariable=password_var, font=("Courier", 12), width=30)
# result_entry.pack(pady=10)
#
# ttk.Button(root, text="Generate Password", command=generate_password).pack()
#
# def copy_to_clipboard():
#     root.clipboard_clear()
#     root.clipboard_append(password_var.get())
#     root.update()
#
# ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
#

root.mainloop()