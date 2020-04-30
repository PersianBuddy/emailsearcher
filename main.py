#! Python 3
# main.py - finds all email addresses

import re
sample_string = 'sdfhk , ckxdf fsds23fm@sd32f.cowefsdfsd3m dskf sdf@gmail.com sfjskdj'

# TODO: create email regular expretion
phone_reg_ex = re.compile('[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}', re.VERBOSE)

# TODO: Find matches
result = re.findall(phone_reg_ex,sample_string)

# TODO: show mathces or export them in a file
print(result)