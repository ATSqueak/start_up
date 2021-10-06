'''
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.


1) user inputs password

2) check password for RE
    at least 8 characters
    upper and lower case.
    1 or more digits
    no spaces
    
Tried this but it will not work:

pwdRegex = re.compile(r'(
[a-zA-Z0-9@#$%^&+=]{8,12}
)', re.VERBOSE)

As need to check each password-restriction separately.
'''

import re

print('This is a password checker')
print('Password needs to be at least 8 characters long and less than 12 characters')
print('It must contain upper and lower case characters')
print('It must contain at least one digit.')



pwd = input('Please enter your password:-  ')

# use a flag to determine at each stage whether the password is valid or not
flat = 0
while True:
    if len(pwd) < 8 and len(pwd) > 12:
        print('Your password must be at least 8 characters long and less than 12 characters')
        flag = -1
        break
    elif not re.search('[a-z]', pwd):
        print('Password must contain at least one lower case character')
        flag = -1
        break
    elif not re.search('[A-Z]', pwd):
        print('Password must contain at least one upper case character')
        flag = -1
        break
    elif not re.search('[0-9]', pwd):
        print('Password must contain a number')
        flag = -1
        break
    elif not re.search('[@#$%^&+=]', pwd):
        print('Password must contain at least one special character')
        flag = -1
        break
    elif re.search('\s', pwd):
        print('No spaces!')
        flag = -1
        break
    else:
        flag = 0
        print('Good password')
        print(pwd)
        break
if flag == -1:
    print('Password not so good')
