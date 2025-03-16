import tkinter as tk #this imports the library we use for GUI
from tkinter import Label, Entry, Button, StringVar, ttk #this indicates which functions we will use from tk
from PIL import Image, ImageTk #signifies use of particular functions within Pillows


def calculate_grade(): #we are creating a function, which will be used as a command for our button later
    try:
        score = float(score_entry.get()) #takes the user input from the entry box and saves input as 'score', computer will recognize 'score' later on as the user's input
        student_type = student_type_var.get() #takes the user input from the entry box and saves user input as 'student_type', computer will recognize 'student_type' later on as the user's input here
        name = name_entry.get() #takes the user input from the entry box and saves user input as 'name_entry', computer will recognize 'name_entry' later on as the user's input

        if student_type == "Undergraduate": #checking to see if user input matches "Undergraduate" exactly, if so, it proceeds with the following if and else if tests
           #the following if criteria are used to determine the output to the user.
            if score >= 95:
                grade = "A+" #if user input is above 95, then output returned to user will be 'A+'
            elif score >= 89.5: #- This assumes that there are round ups to determine final grade
                grade = "A" #if user input is above 89.5, then output returned to user will be 'A'
            elif score >= 84.5:
                grade = "B+" #if user input is above 84.5, then output returned to user will be 'B+'
            elif score >= 79.5:
                grade = "B" #if user input is above 79.5, then output returned to user will be 'B'
            elif score >= 69.5:
                grade = "C" #if user input is above 69.5, then output returned to user will be 'C'
            else:
                grade = "C"
        else:  # These are calculations for Graduate student, since there are only two options to select from in the student_type entry box, if it is not Undergrad, then must be Grad student
            if score >= 89.5:
                grade = "A" #if user input is above 89.5, then output returned to user will be 'A'
            elif score >= 79.5:
                grade = "B" #if user input is above 79.5, then output returned to user will be 'B'
            elif score >= 69.5:
                grade = "C" #if user input is above 69.5, then output returned to user will be 'C'
            else:
                grade = "D" #Based on these grading terms, any number beneath 69.5 will be counted as a 'D'

        result_label.config(text=f"Thank you {name}, here is your final grade: {grade}", fg="red") #This is the output/result returned to the user, including the stored name and grade variable, fg is the color of the font. This utilizes a variable that is created at the bottom of the code.
    except ValueError:
        result_label.config(text="Invalid input! Please enter a numeric score.", fg="red") #If user accidently enters letters into the score entry box, it will tell the user to fix this input


# Create the main window
root = tk.Tk() #opens the GUI
root.title("CSUMB Grade Calculator") #title of the GUI, displayed at top of the window
root.geometry("400x400") #size of the GUI


logo_path = "C:\\users\\johnb\\PycharmProjects\\PythonProject1\\logo1.jpg" #The address to the file we wish to use as the logo, is saved to the variable 'logo_path'
image = Image.open(logo_path) #opens the image in the 'logo_path' variable
image = image.resize((100, 100), Image.LANCZOS) #This resizes the picture file into something that fits in our GUI, LANCZOS helps retain img quality when shrinking
logo = ImageTk.PhotoImage(image) #saves the resized picture into an TK friendly image called 'logo'
logo_label = Label(root, image=logo) #creates a label with the TK friendly image called 'logo', and saves the label as 'logo_label'
logo_label.pack() #pack automatically arranges the label within the Tkinter window

# Input fields
Label(root, text="Student Name:").pack() #Displays label to the user, indicating what the user should enter into the entry box
name_entry = Entry(root) #Creates a name (variable) for the entry box
name_entry.pack() #displays entrybox within the Tkinter window

Label(root, text="Enter Score:").pack() #Displays label to the user, indicating what the user should enter into the entry box
score_entry = Entry(root) #Creates a name (variable) for the entry box
score_entry.pack() #displays entrybox within the Tkinter window

# Dropdown for student type
Label(root, text="Select Student Type:").pack() #Displays label to the user, indicating what the user should enter into the entry box
student_type_var = StringVar() #allows string values to be stored within entry box to newly created variable "student_type_var"
student_type_dropdown = ttk.Combobox(root, textvariable=student_type_var, values=["Undergraduate", "Graduate"]) #creates dropdown list of options for user to select from within the student_type entry box
student_type_dropdown.pack() #displays this entry box within the Tkinter window

# Calculate Button
calculate_button = Button(root, text="Calculate my letter grade", command=calculate_grade) #creates a button, names it, and assigns a command 'def' to it
calculate_button.pack() #displays the button within the Tkinter window

# Label to show result
result_label = Label(root, text="")#creates a new label to display output to user, used in above code.
result_label.pack() #displays within window

# Run the GUI
root.mainloop() #opens window and begins event loop, continuously runs window until user closes it.


