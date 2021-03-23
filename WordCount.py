'''

Ask user for some thoughts

Also word count the contents of a file
open a file
read only
count words
close file

'''
import os

#print(os.getcwd())
thoughts = input('What is on your mind today? ')
result = len(thoughts.split())
print('Great you told me that in {} words'.format(result))

try:
    if os.path.isfile('test.txt'):
        print('Let\'s see how many words are in our file')
        f = open("test.txt", 'r')
        numofwords = f.read()
        print('The number of words in file {} is {} '.format(f.name, len(numofwords.split())))
    else:
        print('Could not find file')
finally:
    f.close()

