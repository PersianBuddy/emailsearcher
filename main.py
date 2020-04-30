#! Python 3
# main.py - finds all email addresses

import re , pyperclip

# user guid
print('Copy your text so it saves into clipboard')
user_response = input('Are you ready? y=\'yes\' n=\'no\' :')
while str(user_response).lower() != 'y':
    user_response = input("Make sure type 'y' when you copied your desired text :")

# take text from clipboard
sample_string = str(pyperclip.paste())

phone_reg_ex = re.compile('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', re.VERBOSE)

emails_list = re.findall(phone_reg_ex, sample_string)
# convert list of emails to a string of emails
emails_string = ''
if len(emails_list) > 0:
    for email in emails_list:
        emails_string += email + '\n'
    pyperclip.copy(emails_string)
    print('\nThese email addresses copied to your clipboard so you can paste it anywhere')
    print('All email addresses available in your desired text')
    print(emails_string)
else:
    print('\nThere is no email address in your desired text')
    print('Or maybe you just forgot to copy your desired text')