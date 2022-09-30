#!/usr/bin/python3
import re, pyperclip, sys


dateRegex = re.compile(r'''(
    ([0-3]\d)         #days from 01 to 31
    /
    ([01]\d)       #months from 01 to 12
    /
    ([12]\d{3})       #Years from 1000 to 2999
    )''', re.VERBOSE)


text = str(pyperclip.paste())

day = []
month = []
year = []
valid_date = []

for date in dateRegex.findall(text):

    if int(date[3]) % 400 == 0 and int(date[3]) % 100 ==0 and int(date[3]) % 4 == 0:
        print('It is a leap year')
        if date[2] in ['04', '06', '09', '11']:
            if int(date[1]) <= 30:
                day.append(date[1])
            else:
                print(f' month {date[2]} should not more than 30 days ')
        elif date[2] == '02':
            if int(date[1]) <= 29:
                day.append(date[1])
            else:
                print('Feb month should not exceed 29 days')
        elif int(date[2]) > 12:
            print('you have only 12 months in the year , not more')
        else:
            if int(date[1]) <= 31:
                day.append(date[1])
            else:
                print('max number of days are 31 days')

    else:
        if date[2] in ['04', '06', '09', '11']:
            if int(date[1]) <= 30:
                day.append(date[1])
            else:
                print(f' month {date[2]} should not more than 30 days ')
        elif date[2] == '02':
            if int(date[1]) <= 28:
                day.append(date[1])
            else:
                print('Feb month should not exceed 28 days')
        elif int(date[2]) > 12:
            print('you have only 12 months in the year , not more')
            #sys.exit()
        else:
            if int(date[1]) <= 31:
                day.append(date[1])
            else:
                print('max number of days are 31 days')

    if int(date[2]) > 12:
        print('you have only 12 months in the year , not more')
    else:
        month.append(date[2])

    year.append(date[3])
    valid_date.append('-'.join([date[1], date[2], date[3]]))

"""try:
    print(text.groups())
    print(text.group(2))
except AttributeError:
    print('Check the date')"""

print(day, month, year)

if len(valid_date) > 0:
    pyperclip.copy('\n'.join(valid_date))
    print('Copied to clipboard')
    print('\n'.join(valid_date))
else:
    print('No birthdate found.')
#4,6,9,11 months = 30 days