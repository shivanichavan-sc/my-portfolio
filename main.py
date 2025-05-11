

import os
import tkinter as tk
from tkinter import ttk, messagebox
import json

class ModernTodo:
    def __init__(self, master):
        self.master = master
        self.master.title("Modern To-do List")
        self.master.geometry("400x500+600+200")
        self.master.configure(bg="#f0f0f0",cursor = "circle", relief = "raised")
        # self.master.resizable(width=True, height=False)
        # if this is not set then it can be resized from both sides
        self.master.iconbitmap("C:\\Users\Shivani\Downloads\iconfinder.ico")
        # self.master.maxsize(800, 1000)
        # self.master.minsize(500, 800)
        # self.master.attributes("-alpha", 0.7)
        # self.master.attributes("-topmost", 0.7)
        # self.master.attributes("-fullscreen", 0.7)
        style = ttk.Style()
        style.theme_use("clam")
        # print(style.theme_use())
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TButton", padding=10, font=('Helvetica', 10))
        # Sets the background color of all ttk.Frames to light gray
        # padding=10: Adds internal spacing (padding) around the button's text.
        # font=('Helvetica', 10): Sets the font to Helvetica, size 10
        # style.map("TButton", foreground=[('pressed', 'red'), ('active', 'green')],
        #           background=[('pressed', 'lightgrey'), ('active', 'blue')])
        style.configure("TEntry", padding=10, font=('Helvetica', 10))
        # Text input field: TEntry padding=10: Adds padding inside the entry box.
        # font=('Helvetica', 10): Makes input text more readable.
        style.configure("Treeview", font=('Helvetica', 10), rowheight=27)
        # ttk.Treeview — a widget used to display tables/lists (like a file explorer or task list).
        # font=('Helvetica', 10): Sets font for each row.
        # rowheight=25: Sets the height of each row in the Treeview (default is often too small)
        style.configure("Treeview.heading", font=('Helvetica', 11, 'bold'))
        # The column headers of the ttk.Treeview
        # font=('Helvetica', 11, 'bold'): Makes the heading labels bold and slightly larger

        self.frame = ttk.Frame(self.master, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        # fill=tk.BOTH means fill both width & height.
        # expand=True means it stretches with window resize

        self.task_var = tk.StringVar()
        # self.task_var.set("Hello!")
        # When run it automatically writes Hello! in the entry box
        self.task_entry = ttk.Entry(self.frame, textvariable=self.task_var, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, sticky="ew")

        self.add_button = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_tree = ttk.Treeview(self.frame, columns=("Task",), show="headings", height=15)
        self.task_tree.heading("Task", text="Tasks")
        self.task_tree.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_tree.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        self.task_tree.configure(yscrollcommand=scrollbar.set)

        self.delete_button = ttk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=10, sticky="ew")

        self.save_button = ttk.Button(self.frame, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.load_tasks()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.task_tree.insert("", tk.END, values=(task,))
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            self.task_tree.delete(selected_item)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def save_tasks(self):
        tasks = [self.task_tree.item(child)['values'][0] for child in self.task_tree.get_children()]
        with open("task.json", "w") as f:
            json.dump(tasks, f)

    def load_tasks(self):
        try:
            with open("task.json", "r") as f:
                tasks = json.load(f)
            for task in tasks:
                self.task_tree.insert('', tk.END, values=(task,))
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernTodo(root)
    root.mainloop()