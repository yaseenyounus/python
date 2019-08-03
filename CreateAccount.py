# Yaseen Younus
# 3 August 2019
# This program take a users email formatted "firstName.lastName@company.com" and creates account credentials for them

import sys
import string
import random

def passwordGenerator():
    password_chars = string.ascii_letters + string.digits + string.punctuation
    print("".join(random.choice(password_chars) for i in range(16)))

def namesFromEmail(user_email):
    first_name = user_email[:user_email.find('.')].capitalize()
    last_name = user_email[user_email.find('.') + 1:user_email.find('@')].capitalize()
    print(f'{first_name} \n{last_name}\n{user_email}')
    

sys.argv.pop(0)
for i in sys.argv:
    namesFromEmail(i)
    passwordGenerator()
    print()
