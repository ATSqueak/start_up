# python3
# phoneAndEmail.py finds phone numbers and email addresses from copied text

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? #area code
(\s|-|\.)?          #separator
(\d{3})             #first 3 digits
(\s|-|\.)           #separator
(\d{4})             #last four digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+   #username
@                   #@ symbol
[a-zA-Z0-9.-]+      #domain name
(\.[a-zA-Z]{2,4})   #dot something
)''', re.VERBOSE)

# http or https with a .com or .org end
webRegex1 = re.compile(r'''(
[http|https]+       #hyper text transfer protocol
:                   #colon
//                  #two forward slashes
[a-zA-Z0-9]+        #website name
(\.[a-zA-Z]{2,3})
)''', re.VERBOSE)

# www.flicky.co.uk
webRegex2 = re.compile(r'''(
[www]+
\.
[a-zA-Z0-9]+
(\.[a-zA-Z]{2,3}
\.
[a-zA-Z]{2,3}
))''', re.VERBOSE)

# www.flicky.com
webRegex3 = re.compile(r'''(
[www]+
\.
[a-zA-Z0-9]+
(\.[a-zA-Z]{2,3})
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

for groups in webRegex1.findall(text):
    matches.append(groups[0])

for groups in webRegex2.findall(text):
    matches.append(groups[0])

for groups in webRegex3.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
