# todo_list_gui.py

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack()

clear_button = tk.Button(root, text="Clear All", width=15, command=clear_tasks)
clear_button.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()
