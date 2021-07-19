'''
Create an acronym from a user entered string of words

'''

print('Let\'s create an acronym')
user_string = input('Please enter a string of words:  ')
string_list = user_string.split()
length = len(string_list)
acronym = ''
for i in range(length):
    acronym += (string_list[i][0]).upper()

print('An acronym from your entered phrase is: ' + acronym)
