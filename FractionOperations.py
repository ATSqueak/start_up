'''
Fraction operations
'''

from fractions import Fraction

def add(a,b):
    print('Result of Addition: {0}'.format(a+b))

def subtract(a,b):
    print('Result of Subtraction: {0}'.format(a-b))

def divide(a,b):
    print('Result of Dividing {0} by {1}: {2}'.format(a, b, a/b))

def multiply(a,b):
    print('Result of Multiplication: {0}'.format(a*b))


if __name__ == '__main__':

    while True:
        
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        if op == 'Add':
            add(a,b)
        if op == 'Subtract':
            subtract(a,b)
        if op == 'Divide':
            divide(a,b)
        if op == 'Multiply':
            multiply(a,b)

        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
