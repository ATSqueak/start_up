'''

Rock Paper Scissors

R = Rock
P = Paper
S = Scissors

Player vs. Computer

Computer stores array as ['rock','paper','scissors']
Player enters their choice
Compare Player entry against Computer entry

paper covers rock
rock blunts scissors
scissors cut paper

Alternative:
How to show what beats what?
True/False?
E.g. compare two variables
Or case compare?
if user1 = P and user2 = R then user2 wins as rock cuts paper

'''

import random
computer_choice_array = ['rock','paper','scissors']

print()
print('Do you want to play rock, paper, scissors?')
keep_playing = True
while keep_playing:

    player = input('Enter your choice: ')
    if (player.casefold() not in computer_choice_array):
        print('Not recognised')
    computer_choice = random.choice(computer_choice_array)
    if player == computer_choice:
        print('It is a tie! Player played ' + player + ' and Computer played ' + computer_choice)
    elif player == 'rock' and computer_choice == 'paper':
        print('Computer wins as rock cover paper Player played ' + player + ' and Computer played ' + computer_choice)
    elif player == 'rock' and computer_choice == 'scissors':
        print('Player wins as rock blunts scissors Player played ' + player + ' and Computer played ' + computer_choice)
    elif player == 'scissors' and computer_choice == 'paper':
        print('Player wins as scissors cut paper Player played ' + player + ' and Computer played ' + computer_choice)
    elif player == 'scissors' and computer_choice == 'rock':
        print('Computer wins as rock blunts scissors Player played ' + player + ' and Computer played ' + computer_choice)
    elif player == 'paper' and computer_choice == 'rock':
        print('Player wins as paper covers rock Player played ' + player + ' and Computer played ' + computer_choice)
    elif player == 'paper' and computer_choice == 'scissors':
        print('Computer wins a scissors cut paper Player played ' + player + ' and Computer played ' + computer_choice)

    play = input('Do you want to have another go?')
    if play.casefold() == 'n':
        keep_playing = False
        print('Goodbye thanks for playing')
    elif play.casefold() != 'n' and play.casefold() != 'y':
        keep_playing = False
        print('Goodbye thanks for playing')
        break


