import tkinter as tk #this imports the library we use for GUI
from tkinter import filedialog, Label, Button #this indicates which functions we will use from tk
from PyPDF2 import PdfReader, PdfWriter #indicates which functions we will use from PyPDF2 library


def split_pdf(): #we are creating a function, which will be used as a command for our button later
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")]) #allows user to select only pdfs within files
    if not file_path:
        return #This line of code is used to check if the user has canceled the file selection or if no file was selected, and if so, it exits the current function or process.

    try: #tells computer to try, but if there is an error such as file issue or invalid PDF, then it jumps to except
        reader = PdfReader(file_path) #tells pdfreader to read the file located at 'file_path'
        writer = PdfWriter() #This utilizes pdfwriter to create a new PDF file

        # Add the first page of the original PDF to the new PDF
        writer.add_page(reader.pages[0]) #adds the first page of the read pdf, to the new pdf

        # Save the new PDF
        output_path = "NewPDF.pdf" #saves the newly created PDF as "green text"
        with open(output_path, "wb") as output_pdf: #This line opens the new PDF file for writing. The "wb" means "write in binary mode" (because PDFs are binary files).
            writer.write(output_pdf) #This writes the contents of the first page of the original PDF into the new file (NewPDF.pdf).

        result_label.config(text="Split performed. Please see the new split file.", fg="green") #After successfully splitting the PDF, this line changes the text on a label in the GUI to show a success message
    except Exception as e: #If an error occurs, the program moves to this block.
        result_label.config(text=f"Error: {str(e)}", fg="red") #If there was an error, this line changes the label's text to show an error message, with the error description, in red


# Create the main window
root = tk.Tk() #Opens the GUI
root.title("PDF Splitter") #Displays name of the application at the top of the GUI window
root.geometry("400x200") #establishes the size of the window

# Instruction Label
Label(root, text="Choose a PDF file to split Page 1").pack() #Displays label informing user of instructions

# Button to choose PDF file
split_button = Button(root, text="Select PDF and Split", command=split_pdf) #Creates a button, names it, and assigns it a command as defined earlier under 'def'
split_button.pack() #displays the button in the window

# Label to display the result
result_label = Label(root, text="")  ##creates a new label to display output to user, used in above code.
result_label.pack() #displays the result label

# Run the GUI
root.mainloop() #opens window and begins event loop, continuously runs window until user closes it.

