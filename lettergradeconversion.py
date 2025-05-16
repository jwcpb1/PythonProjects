
number = float(input(f'Hi there. I am a letter grade converter. Tell me, what percentile did you get in your class? '))

if number>=90:
    print("Great job! You received an A")
elif number>=80:
    print("Good job! You received a B")
elif number>=70:
    print("You passed with a C")
elif number>=60:
    print("You got a D. You should check your understanding of the material. Perhaps you should retake the class.")
else:
    print("You failed and received an F. You must retake the course.")
