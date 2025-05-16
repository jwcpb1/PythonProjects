
import random
print("Hi there. Lets play rock paper scissors. If you haven't played before, rock beats scissors. Scissors beats paper. Paper beats rock. Lets go.")
user_action = input("Choose rock, paper, or scissors...  ")
possible_action = ['rock','paper','scissors']
computer_action = random.choice(possible_action)
print('You chose ' + user_action +'. Computer randomly chose ' + computer_action + '.')
if user_action.lower() == computer_action:
    print('We have a draw. Both players selected ' + user_action +'.')
elif user_action.lower()== 'rock':
    if computer_action == 'scissors':
        print('Rock smashes scissors. You win!')
    else:
        print('Paper beats rock. You lose...:/')
elif user_action.lower()== 'scissors':
    if computer_action == 'rock':
        print('Rock smashes scissors. You lose..:/')
    else:
        print('Scissors cuts paper. You Win!')
elif user_action.lower()== 'paper':
    if computer_action == 'rock':
        print('Paper beats rock. You win!')
    else:
        print('Scissors cuts paper. You lose...:/')
