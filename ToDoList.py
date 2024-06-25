from tkinter import *
import tkinter.messagebox as msgbox
from os import remove, rename
def addtask():
    task_list.insert(END, task.get())
    with open("Task.txt", 'a') as f:
        f.write(task.get() + '\n')

def addtaskenter(event):
    addtask()

def deletetask():
    selected_indices = task_list.curselection()
    if selected_indices:
        selected_index = selected_indices[0]
        global selected_item
        selected_item = task_list.get(selected_index)
        task_list.delete(selected_index)

    else:
        msgbox.showinfo("Error", "First select a task to delete!")
        return

    with open("Task.txt", 'r') as f:
        tk = f.readlines()

    for i in tk:
        if i == selected_item:
            tk.remove(selected_item)

    with open("Task2.txt", 'a') as f:
        for i in tk:
            f.write(i)

    remove("Task.txt")
    rename("Task2.txt", "Task.txt")
def deleteall():
    task_list.delete(0, END)
    remove("Task.txt")

def showtasks():
    try:
        with open("Task.txt", "r") as f:
            tk = f.readlines()

    except FileNotFoundError:
        return

    for i in tk:
        task_list.insert(END, i)

root = Tk()

root.title("To-Do List")

root.geometry("400x300")
root.minsize(width=200, height=100)

h1 = Label(root, text="To-Do List", font="Corbel 20 bold")
h1.pack()

f1 = Frame(root)
f1.pack(side=LEFT, padx=40, pady=10)

f2 = Frame(root)
f2.pack(side=LEFT, padx=40, pady=10)

task = StringVar()

field = Entry(f1, textvariable=task)
field.pack(side=TOP)
field.bind('<Return>', addtaskenter)

add_btn = Button(f1, fg='green', command=addtask, text="Add Task", width=16)
add_btn.pack(side=TOP, pady=25)

del_btn = Button(f1, fg='red', command=deletetask, text="Delete Task", width=16)
del_btn.pack(side=TOP)

del_all_btn = Button(f1, fg='blue', command=deleteall, text="Delete All Tasks", width=16)
del_all_btn.pack(side=TOP, pady=25)

task_list = Listbox(f2)
task_list.pack()

showtasks()

root.mainloop()