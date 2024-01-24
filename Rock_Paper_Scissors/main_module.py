import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Please choose [r]ock, [p]aper or [s]cissors: ')

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid input. Please try again ...')

computer_move = ''

random_integer = random.randint(1, 3)

if random_integer == 1:
    computer_move = rock
elif random_integer == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f'Computer move is {computer_move}.')

if player_move == rock:
    if computer_move == rock:
        print('Draw!')
    elif computer_move == paper:
        print("Computer wins!")
    elif computer_move == scissors:
        print('You win!')
elif player_move == paper:
    if computer_move == rock:
        print('You win!')
    elif computer_move == paper:
        print("Draw!")
    elif computer_move == scissors:
        print('Computer wins!')
elif player_move == scissors:
    if computer_move == rock:
        print('Computer wins!')
    elif computer_move == paper:
        print("You win!")
    elif computer_move == scissors:
        print('Draw!')

play_again = input('Do you want to play again y/n: ')

if play_again == 'y':


