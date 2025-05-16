dollars = input("How many US dollars do you wish to transfer to Nepal? ")

answer=input(f'Please confirm..Is this number in USD or rupees? ')

if answer.lower()=="usd":
    converted = float(dollars)*120
    print(f'Thank you for your contribution! You contributed {converted} rupees. We hope to see you again!')
else:
    print(f'Thank you for contributing {dollars} rupees! Pleasure doing business.:)')


