#------------------------------------------------------------------------------------------
#AUDIOBOOK

#Creating Audio Book out of PDF without GUI
#We are creating an Audio Book that reads a PDF file from our computer

#pip install gtts
#pip install pypdf2
#you don’t need to install anything for import os. The os module is a built-in Python library,
# meaning it comes pre-installed with Python. You can use it directly without any additional installation.

from gtts import gTTS  # Import gTTS (Google Text-to-Speech) to convert text to speech
from PyPDF2 import PdfReader  # Import PdfReader to read PDF files
import os  # Import os module to interact with the operating system

# Open the PDF file in binary read mode
book = open('groupproject.pdf',) #mislead is the name of the PDF file that I have in my pythonProject2 folder in Computer

# Create a PdfReader object to read the PDF
pdfReader = PdfReader(book)

# Get the total number of pages in the PDF
pages = len(pdfReader.pages)

# Initialize an empty string to store the text of the entire PDF
full_text = ""

# Loop through all pages of the PDF and extract text
for num in range(pages):  # Iterate through each page
   page = pdfReader.pages[num]  # Get the current page
   text = page.extract_text()  # Extract text from the page
   if text:  # Check if text extraction was successful
       full_text += text  # Append extracted text to the full text string (i.e., full_text = text +1)

# Close the PDF file after reading
book.close()

# Convert the full extracted text to speech using gTTS
tts = gTTS(text=full_text, lang='en')  # Convert text to speech in English
#also, if you want to slow the speed of the voice, change the code above to:
#tts = gTTS(text=full_text, lang='en', slow=False) # Set slow=True for slower speech, False for normal

# for British accent, change the line of the code above to:
#tts = gTTS(text=full_text, lang='en', tld='co.uk')  or to co.au for Australian or co.in for indian

# Save the speech as a single MP3 file
tts.save("project_guideline.mp3")  # Save the generated speech to an MP3 file

# Play the saved MP3 file using the default system media player
print("Playing the audiobook...")  # Inform the user that playback is starting
os.startfile("project_guideline.mp3")

#***************************************************************************************

