'''

Write a function named collatz() that has one parameter named number. If number is even,
then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.

'''


def collatz(number):
    if number % 2 == 0:
        print(number //2)
        return number // 2
    elif number % 2 == 1:
        print(number*3 + 1)
        return 3 * number + 1


print('Play Collatz')
try:
    user_entered_num = input('Please enter a number ')
    while user_entered_num != 1:
        user_entered_num = collatz(int(user_entered_num))
except ValueError:
    print('Error! Please enter an integer number')
