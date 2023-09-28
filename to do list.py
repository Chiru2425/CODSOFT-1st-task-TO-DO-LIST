import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    task_list.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and configure the task list
task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, font=("Helvetica", 12))
task_list.pack(pady=10)

# Create and configure the task entry
task_entry = tk.Entry(root, font=("Helvetica", 12))
task_entry.pack(pady=5)

# Create buttons to add, delete, and clear tasks
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Helvetica", 12))
delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Helvetica", 12))
clear_button = tk.Button(root, text="Clear All", command=clear_tasks, font=("Helvetica", 12))

add_button.pack(pady=5)
delete_button.pack(pady=5)
clear_button.pack(pady=5)

root.mainloop()