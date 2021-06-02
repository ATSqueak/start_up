'''

Ask the user to give you five words. Then check if any of the five words is a palindrome.

A palindrome is a word that remains the same whether it's read forward or backward.
e.g. madam is a palindrome

'''


print('Let us play the palindrome game')

user_five_words = input('Please enter five words (separated by spaces): ')
list_text = user_five_words.split(' ')
length_of_array = len(list_text)
if length_of_array != 5:
    print('You have not entered five separate words')
print('You entered the words: ', list_text)
for i in range(length_of_array):
    individual_word = list_text[i]
    reverse_individual_word = individual_word[::-1]
    if individual_word.isalpha():
        if individual_word == reverse_individual_word:
            print('The word "{}" is a palindrome'.format(individual_word))
        else:
            print('The word "{}" is not a palindrome'.format(individual_word))
    else:
        print('The entered value "{}" is not a word'.format(individual_word))

