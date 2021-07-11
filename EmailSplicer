'''Email slicer
Collect an email address from the user and then find out if the user has a custom domain name or a popular domain name. For example:

Input: mary.jane@gmail.com
Output: Hey Mary, I see your email is registered with Google. That's cool!.
Input: peter.pan@myfantasy.com
Output: Hey Peter, looks like you've got your own custom setup at MyFantasy. Impressive!.
'''

print('This is an email slicer program')
known_domains={"gmail":"Google","yahoo":"Yahoo","hotmail":"Microsoft","outlook":"Microsoft"}
#strip will remove trailing and leading spaces
email = input('Please enter your email address here: ').strip()
print(email)
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
domain = domain[:domain.index('.')]
#print(f'Your username is {username} and your domain is {domain}')
if domain in known_domains.keys():
    print(f'Hello {username} looks like your domain is with {known_domains[domain]}')
else:
    print(f'Hello {username} looks like you have your own domain at {domain}')
