from tkinter import *  # Import everything from the Tkinter library
import datetime
root = Tk()  # Create the main application window (root window)
root.title("Age Calculator")  # Set the window title
root.geometry("400x200")  # Set window size as a string "widthxheight"


#below, we are creating a def function that clculates birthdate based on entrybox, then calculates age and then presents it in a label
#we will recall this def function in our BUTTON function later
def calculateage():
 birthdate = datetime.datetime(int(YearVariable.get()), int(MonthVariable.get()), int(DayVariable.get()))
 age = datetime.datetime.now() - birthdate
 convertdays = int(age.days)
 ageyears = round(convertdays / 365, 2)
 Label(text=f"{NameVariable.get()} your age is {ageyears}").grid(row=6, column=1)

lb1 = Label(root, text = "Your Name" ).grid(row=1, column=1, padx=90)
lb2 = Label(root, text = "Year" ).grid(row=2, column=1, padx=90)
lb3 = Label(root, text = "Month").grid(row=3, column=1, padx=90)
lb4 = Label(root, text = "Day" ).grid(row=4, column=1, padx=90)
#note: padx=90 adds horizontal padding (extra space) on both sides of the widget. It means there will be 90 pixels of empty space to
# the left and right of the label. This helps in adjusting the layout and making the UI look better.

NameVariable = StringVar()
YearVariable = StringVar()
MonthVariable = StringVar()
DayVariable = StringVar()
EntryName = Entry(root, textvariable= NameVariable).grid(row=1, column=2)
EntryYear = Entry(root, textvariable= YearVariable).grid(row=2, column=2)
EntryMonth = Entry(root, textvariable= MonthVariable).grid(row=3, column=2)
EntryDay = Entry(root, textvariable= DayVariable).grid(row=4, column=2)

button1 = Button(root, text="Submit", command = calculateage) #calculateAGE is our Def funciton we are recalling.
button1.grid(row=5, column=1)

root.mainloop()  # Use root.mainloop() instead of mainloop()



#CHATGPT ADJUSTED

from tkinter import *  # Import everything from the Tkinter library
import datetime

root = Tk()  # Create the main application window (root window)
root.title("Age Calculator")  # Set the window title
root.geometry("400x200")  # Set window size as a string "widthxheight"

# Dictionary to map month names to numbers
month_mapping = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12
}


def calculateage():
    try:
        month_input = MonthVariable.get().strip().lower()
        if len(month_input) < 4 and not month_input.isdigit():
            Label(text="Please enter entire word for month.").grid(row=6, column=1)
            return
        month = month_mapping.get(month_input, month_input)  # Convert if it's a name
        month = int(month)  # Ensure it's an integer

        birthdate = datetime.datetime(int(YearVariable.get()), month, int(DayVariable.get()))
        age = datetime.datetime.now() - birthdate
        convertdays = int(age.days)
        ageyears = round(convertdays / 365, 2)
        Label(text=f"{NameVariable.get()} your age is {ageyears}").grid(row=6, column=1)
    except ValueError:
        Label(text="Invalid date input! Please enter a valid date.").grid(row=6, column=1)
    except KeyError:
        Label(text="Invalid date input! Please enter a valid date.").grid(row=6, column=1)


lb1 = Label(root, text="Your Name").grid(row=1, column=1, padx=90)
lb2 = Label(root, text="Year").grid(row=2, column=1, padx=90)
lb3 = Label(root, text="Month").grid(row=3, column=1, padx=90)
lb4 = Label(root, text="Day").grid(row=4, column=1, padx=90)

NameVariable = StringVar()
YearVariable = StringVar()
MonthVariable = StringVar()
DayVariable = StringVar()
EntryName = Entry(root, textvariable=NameVariable).grid(row=1, column=2)
EntryYear = Entry(root, textvariable=YearVariable).grid(row=2, column=2)
EntryMonth = Entry(root, textvariable=MonthVariable).grid(row=3, column=2)
EntryDay = Entry(root, textvariable=DayVariable).grid(row=4, column=2)

button1 = Button(root, text="Submit", command=calculateage)
button1.grid(row=5, column=1)

root.mainloop()
