# A quick dice rolling game!
import random
print('Pick a number between 1 and 6')
user_number = int(input())
random_number = random.randint(1, 6)
print('User number: ' + str(user_number))
print('Computer number: ' + str(random_number))
if user_number > random_number:
    print('You win!')
elif user_number == random_number:
    print('It is a draw!')
else:
    print('You lose!')
