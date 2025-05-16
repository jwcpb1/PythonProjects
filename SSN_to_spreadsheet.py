from tkinter import *
from tkinter import messagebox
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google sheet setup for integration
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("final-460020-5ffcb4ff346a.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Benefit").sheet1  # Opens the first worksheet in the "Benefit" spreadsheet

# export function command
def submit_data():
    ssn = NumberVariable.get()
    name = NameVariable.get()
    address = AddressVariable.get()
    age = AgeVariable.get()

    # Basic troubleshoot
    if not (ssn and name and address and age): #checks for missing input in entry boxes
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        int(age)
    except ValueError:
        messagebox.showerror("Input Error", "Age must be a number.")
        return #in case the input in age is not a number

    # add data in new row in spreadsheet
    sheet.append_row([ssn, name, address, age])
    messagebox.showinfo("Success", "Data submitted successfully!")

    # Clear entry boxes
    NumberVariable.set("")
    NameVariable.set("")
    AddressVariable.set("")
    AgeVariable.set("")

#GUI setup
root = Tk()
root.title("Benefit Form")  # Updated title to match screenshot
root.geometry("400x200")
root.configure(bg="white")  # Optional: white background like the screenshot

# Defining our key variabels
NumberVariable = StringVar()
NameVariable = StringVar()
AddressVariable = StringVar()
AgeVariable = StringVar()

# Labels with aesthetic placement
Label(root, text="Social Security Number", anchor="e", width=20).grid(row=1, column=1, padx=(10, 10), pady=5, sticky="e")
Label(root, text="Full Name", anchor="e", width=20).grid(row=2, column=1, padx=(10, 10), pady=5, sticky="e")
Label(root, text="Your Address", anchor="e", width=20).grid(row=3, column=1, padx=(10, 10), pady=5, sticky="e")
Label(root, text="Your age", anchor="e", width=20).grid(row=4, column=1, padx=(10, 10), pady=5, sticky="e")

# User Entry Boxes with aesthetic placement
Entry(root, textvariable=NumberVariable, width=30).grid(row=1, column=2, padx=(0, 20), pady=5)
Entry(root, textvariable=NameVariable, width=30).grid(row=2, column=2, padx=(0, 20), pady=5)
Entry(root, textvariable=AddressVariable, width=30).grid(row=3, column=2, padx=(0, 20), pady=5)
Entry(root, textvariable=AgeVariable, width=30).grid(row=4, column=2, padx=(0, 20), pady=5)

# Submit button centered below inputs
Button(root, text="Submit", width=10, command=submit_data).grid(row=5, column=2, pady=10)

#Run GUI until manually closed.
root.mainloop()
