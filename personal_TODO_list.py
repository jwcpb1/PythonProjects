import tkinter as tk  #imports Python’s tkinter module used for GUI
from tkinter import messagebox  #imports submodule within tkinter used for pop up dialogue boxes

def add_task():  #creation of a command and assigning it a name that will be called on later
    task = task_entry.get()   #the get function retrieves user input from the tk input box called 'task_entry' see below. This input is saved to the variable 'task'
    if task: #beginning of if statement, if there is a task inputed into the entry box
        task_listbox.insert(tk.END, task) #insert function inserts 'task' to the end of the listbox (created down below)
        task_listbox.itemconfig(tk.END, {'fg': 'red'})  #itemconfig function is used to change appearence of elements (text) In this case, it makes the newly added task red
        task_entry.delete(0, tk.END)  #delete function is used to delete or clear the input in the user entry box after the command has been executed. This makes it ready for the user's next input.
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!") #if no entry is made to the entry box, a popup message warning notifies user that command cannot be done because entry box is empty.

def remove_task(): #creation of a command and assigning it a name that will be called on later
    try:
        selected_task_index = task_listbox.curselection()[0] # Gets the index of the currently selected task in the listbox
        task_listbox.delete(selected_task_index) # Deletes the task at the selected index from the listbox
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!") # Shows a warning if no task was selected before trying to delete

def mark_completed(): #creation of a command and assigning it a name that will be called on later
    try:
        selected_task_index = task_listbox.curselection()[0] #Again, this gets the index of the selected task
        task = task_listbox.get(selected_task_index) #The get function here retrieves the task text at that index
        task_listbox.delete(selected_task_index) #The delete function deletes the selected index
        task_listbox.insert(selected_task_index, f"✔ {task}") #This insert function inserts the exact same previously deleted task in the same position, with a checkmark next to it.
        task_listbox.itemconfig(selected_task_index, {'fg': 'green'})  # This changes the newly inserted index format to the font color green.
    except IndexError:
        messagebox.showwarning("Warning","No task selected!") # Shows a warning if no task was selected before trying to mark complete

#My Code from class notes
root = tk.Tk()  #creates a main window
root.title("Productivity Task Manager") #top title of GUI popup
root.geometry("400x400") #size of the GUI popup

title_label = tk.Label(root, text="What do you need to do today?", font=("Helvetica", 14, "bold")) #this creates a top displayed title label, in bold text.Reminds user what to do
title_label.pack(pady=10) #this pack function, tells tkinter how to geometrically display the label, in this case, there is a 10 pixel padding above, and below the label

task_entry = tk.Entry(root, width=40) #tk.Entry creates an input box within the GUI, and the width is how many characters long it is. Then it is assigned to the variable 'task_entry'
task_entry.pack(pady=10) #the pack function displays entry box on screen, telling the computer to put a 10 pixel padding above and below the entry box.

add_button = tk.Button(root, text="Add Task", command=add_task) #creation of a tk button, assigning it a name and command (see earlier def functions), and assigning it to a variable
add_button.pack() #the pack function actually displays the button on the screen.

remove_button = tk.Button(root, text="Remove Task", command=remove_task) #creation of a tk button, inputs it into GUI, names it, and assigns a def command from earlier.
remove_button.pack() #the pack function actually displays the button on the screen.

complete_button = tk.Button(root, text="Mark Completed", command=mark_completed) #creation of a tk button, inputs it into GUI, names it, and assigns a def command from earlier.
complete_button.pack() #the pack function actually displays the button on the screen.

task_listbox = tk.Listbox(root, width=50, height=15) #creation of a tkinter listbox, which stacks listable items on top of each other. It adds this to the GUI with root, and the size of the box are given. This is critical for the 'add_task' and 'remove_task' functions since this is where the change is recorded.
task_listbox.pack(pady=10) #the pack function actually displays the button on the screen, tells computer to add 10 pixel buffer (padding) above and below

root.mainloop() #starts the event loop, and keeps it going until user closes GUI