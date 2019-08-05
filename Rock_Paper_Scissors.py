import random
print('Rock, Paper or Scissors')
c_option = random.randint(1, 3)
option = str(input()).upper()


# if (option != 'ROCK' or 'PAPER' or 'SCISSORS'):
#    print('This is rock, paper or scissors, please use ROCK, PAPER or SCISSORS.')

print('User: ' + option)

if c_option == 1 and option == 'PAPER':
    print('Computer: Rock')
    print('You win!')
elif (c_option == 1 and option == 'SCISSORS'):
    print('Computer: Rock')
    print('You lose!')
elif (c_option == 1 and option == 'ROCK'):
    print('Computer: Rock')
    print('Draw!')
elif (c_option == 2 and option == 'ROCK'):
    print('Computer: Paper')
    print('You lose!')
elif (c_option == 2 and option == 'SCISSORS'):
    print('Computer: Paper')
    print('You win!')
elif (c_option == 2 and option == 'PAPER'):
    print('Computer: Paper')
    print('Draw!')
elif (c_option == 3 and option == 'ROCK'):
    print('Computer: Scissor')
    print('You win!')
elif (c_option == 3 and option == 'PAPER'):
    print('Computer: Scissor')
    print('You lose!')
elif (c_option == 3 and option == 'SCISSORS'):
    print('Computer: Scissor')
    print('Draw!')
else:
    print('This is rock, paper or scissors, please use ROCK, PAPER or SCISSORS.')
