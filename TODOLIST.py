from tkinter import *
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter a task!")

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showerror("Error", "Please select a task to remove!")

def clear_tasks():
    task_list.delete(0, END)

root = Tk()
root.title("To-Do List")
root.geometry("400x300")

task_list = Listbox(root, selectmode=SINGLE)
task_list.pack(pady=10)

entry = Entry(root)
entry.pack(pady=5)

add_button = Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

clear_button = Button(root, text="Clear All", command=clear_tasks)
clear_button.pack(pady=5)

root.mainloop()
