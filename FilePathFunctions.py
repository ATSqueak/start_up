'''
A few functions to manage files and directories
'''
import os


# get current working directory
def getcurrentdir():
    return os.getcwd()


# change directory
def changedir(s):
    try:
        return os.chdir(s)
    except ValueError:
        print('This directory does not exist')


# join to list multiple files in a directory
def joinpath(s):
    for name in s:
        print(os.path.join('/Users/arif/test_project', name))


fileNames = ['doc1.txt', 'doc2.txt', 'doc3.txt']
joinpath(fileNames)
print(getcurrentdir())
