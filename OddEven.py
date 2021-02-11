'''
Hello <User>
Start Loop
Please provide a number between 1 and 1000
test if truly an INT
Is the number odd or even
Print number is odd or even
Do you want to play again?

'''

user = input('Hi what is your name?\n')
print('Hello {}'.format(user))
keep_playing = True
while keep_playing:
    try:
        number = int(input('Please give me a number between 1 and 1000:'))
    except ValueError:
        print('Error: You did not input an integer')
        break

    string_error = int(number)

    if number < 0:
        print('Number too low!')
    elif number > 1000:
        print('Number is too high')
    elif (number % 2) == 0:
        print('This is an even number')
    else:
        print('This is an odd number')

    play = input('Do you want to have another go?')
    if play.casefold() == 'n':
        keep_playing = False
        break

