#! Python 3
# main.py - finds all email addresses

import re , pyperclip

# take text from clipboard
sample_string = str(pyperclip.paste())

phone_reg_ex = re.compile('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', re.VERBOSE)

emails_list = re.findall(phone_reg_ex, sample_string)
# convert list of emails to a string of emails
emails_string = ''
if len(emails_list) > 0:
    for email in emails_list:
        emails_string += email + '\n'

print(emails_string)