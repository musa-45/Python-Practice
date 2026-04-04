

import random
emojis = {'r':'✊', 'p':'✋', 's':'✌️'}
choices = ['r', 'p', 's']
while True:
 user_choice = input('Rock,paper,scissors? (r/p/s): ').lower()

 if user_choice not in choices:
    print('Ivalid choice. Please enter r, p, or s.')
    continue

    #print('Invalid choice. Please enter r, p, or s.')
 computer_choice = random.choice(choices)
 print(f'You choose {emojis[user_choice]}')
 print(f'Computer choose {emojis[computer_choice]}')

 if user_choice == computer_choice:
    print('It is a tie!')   
 elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
    print('You win!')
 else: 
    print('Computer wins!')

 should_continue = input('Play again? (y/n): ').lower()
 if should_continue == 'n':
        print('Thanks for playing!')
        break
 elif should_continue != 'y':
        print('Invalid choice. Please enter y or n.')
