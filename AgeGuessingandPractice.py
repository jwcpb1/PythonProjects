weight = input('What is your weight? ')
unit = input('Is your weight in LBS or KILOS? Answer one or the other ')

if unit.lower()=="lbs":
    converted = float(weight)*0.45
    print("Your weight is " + str(converted) +  " kilograms. ")
else:
    converted = float(weight)/.45
    print(f'Your weight is {converted} pounds.')

print("Thanks for using the app and good job converting your weight.")



for i in range(5):
    print(i)

#list = [apple,orange,banana]   i is same as item and index,,,, i is a variable

fruits = ['apple','orange','banana']
for i in fruits:
    print(i)

prices = [500,300,200]
Total = 0
for i in prices:
    Total = Total+i
print(Total)


Price = 7
while Price<12:
    print(Price)
    Price = Price+1



#Age Guessing Game
age = 22
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess my age: "))
    if guess == age:
        print("Your guess is correct")
        break  # no need to loop. end our code
    else:
        guess_count = guess_count + 1
        if guess_count < guess_limit:
            print("Incorrect guess. Try again")
        else:
            print("Sorry to many attempts")


