'''
Setting a date standard for different date types in a doc...
ISO 8601 tackles this uncertainty by setting out an internationally agreed way to represent dates:
YYYY-MM-DD
For example, September 27, 2012 is represented as 2012-09-27.


such as 3/14/2015, 03-14-2015,
and 2015/3/14)


'''

import re, pyperclip


def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\1-\\2', dt)


dt1 = "2026-01-02"
print("Original date in YYYY-MM-DD Format: ", dt1)
print("New date in DD-MM-YYYY Format: ", change_date_format(dt1))

datePattern = re.compile(r'''(
(\d)/(\d{2})/(\d{4})     #3/14/2015
(\d{2})-(\d{2})-(\d{4})  #03-14-2015
(\d{4})/(\d)/(\d{2})     #2015/3/14
)''', re.VERBOSE)

datePattern.sub()

'''
#Attempt1:
import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))

#Attempt2
text = str(pyperclip.paste())
matches = []

for groups in datePattern.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No dates found')
'''
