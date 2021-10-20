'''

Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string.
Otherwise, the characters specified in the second argument to the function will be removed from the string.

function
first arg = string to be operated on
second arg = character to be stripped

check for second arg at the beginning and end of the first arg
if found then remove from beginning and end of first arg/string
return amended first string

if no second arg then default to space character

First attempt....
stripChar = 'u'
testString = stripChar * 3 + 'thisisATest' + stripChar * 3
print(testString)
if re.search(r'^' + stripChar + '[a-zA-Z]+' + stripChar + '$', testString):
    print('Good')
    print(re.sub(r'^' + stripChar + ' | ' + stripChar + '+$', '', testString))
else:
    print('Bad')

'''

import re

print(
    'This is a copy of the strip function where the character you specify will be stripped from the start and end of a string')

def my_strip(s):
    # return re.sub(r'\s+$', '', re.sub(r'^\s+', '', s))
    print(s)
    if (s[0] == ' '):
        return re.sub(r'^\s+|\s+$', '', s)
    else:
        return re.sub(r'^'+s[0]+'+|'+s[0]+'+$', '', s)


print(my_strip('uuuabcuuu'))
#print(my_strip('   abc   '))
