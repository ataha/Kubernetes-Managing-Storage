#!/usr/bin/python3
import re, pyperclip
import string, random

"""Security is one of the most crucial parts of our lives.
   The importance of security is increasing day by day as most things are going online.
   Passwords come into light as we talk about security.
"""

"""This password generator that helps us generate random and strong passwords quickly.
   It will also check and confirm if this generated password is strong enough"""


# Strong Password Regexes
pass_length_regex = re.compile(r'.{12,}')                   # >= 12 characters
pass_upper_regex = re.compile(r'[A-Z](.*?)[A-Z]')           # Contains at least 2  upper case letter
pass_lower_regex = re.compile(r'[a-z]')                     # Contains a lower case letter
pass_digit_regex = re.compile(r'[0-9](.*?)[0-9]')           # Contains at least 2 digit numbers
pass_char_regex = re.compile(r'[=`~!@#$%^&-+\[{\]}.*/|()_](.*?)[=`~!@#$%^&-+\[{\]}.*/|()_]')   # Contains a special characters

# Function to check the above regexes
def good_pass_check(text):
    if pass_length_regex.search(text) is None:
        print('Not the best password..... ')
        print('Password should contains  >=12 characters, better to change your length choice')
    elif pass_upper_regex.search(text) is None:
        print('Not the best password..... ')
        print('Password should contains at least 2 upper case letters')
    elif  pass_lower_regex.search(text) is None:
        print('Not the best password..... ')
        print('Password should contains lower case letters')
    elif  pass_digit_regex.search(text) is None:
        print('Not the best password..... ')
        print('Password should contains at least 2 digit numbers')
    elif  pass_char_regex.search(text) is None:
        print('Not the best password..... ')
        print('Password should contains at least 2 special characters  =`~!@#$%^&-+[{]}.*/|()_')
    else:
        print('That\'s a strong password. Remember to use it for one site only.')

# Retrieve Password from clipboard
#passWord = str(pyperclip.paste())

# Run it through the function and print relevant message to the console
#good_pass_check(passWord)

characters = list(string.ascii_letters + string.digits + "~!@#$%^&-+[{]}.*/|()_")
def generate_strong_password():
    length = int(input("Enter password length: "))
    passWord = "".join(random.choice(characters) for x in range(length))
    print(f"\nYour New password is:  {passWord}")
    print(".....")
    good_pass_check(passWord)


generate_strong_password()