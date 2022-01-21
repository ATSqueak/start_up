'''

Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and inserted before the last item.
 For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
 But your func- tion should be able to work with any list value passed to it.
'''


def manipulate(listToChange):
    #listToChange.insert(-1, 'and')
    listToChange[-1] = ' and ' + listToChange[-1]
    for i in range(len(listToChange[:-2])):
        listToChange[i] = listToChange[i] + ', '
    print(listToChange)
    name = ''
    for item in range(len(listToChange)):
        name = name + (listToChange[item])
    print('\''+str(name).strip()+'\'')


spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['orange', 'apples', 'noint', 'mint']
#manipulate(spam)
manipulate(spam2)
print(','.join(spam2))
