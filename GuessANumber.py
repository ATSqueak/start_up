'''

You ask a user to guess a number between 1 and 50.

If they guess outside that range, you prompt with an error encouraging them to choose a number within the proper range.

Whenever they guess the wrong number you ask if they want to keep playing or if they'd like to quit.

Finally, when the user eventually guesses the right number you congratulate them and show the number of attempts they had.


'''
import random
print('Let us play guess a number. The range will be between 1 and 50')

attempts = 0
number = random.randint(1,50)
keep_playing = True

while keep_playing:
    try:
        attempts = attempts + 1
        guess = int(input('Guess a number between 1 and 50 '))
        if guess > 50 or guess < 1:
            print('You have guessed outside of the range please choose a number between 1 and 50')
            #break
        elif guess == number:
            print('You guess correctly after {} attempts'.format(attempts))
        elif guess != number:
            print('You are incorrect try again')
    except ValueError:
        print('Error: You did not input an integer')
        break
    play = input('Do you want to have another go?')
    if play.casefold() == 'n':
        keep_playing = False
        print('Goodbye thanks for playing')
    elif play.casefold() != 'n' and play.casefold() != 'y':
        keep_playing = False
        print('Goodbye thanks for playing')
        break
