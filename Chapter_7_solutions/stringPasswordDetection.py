import re

longPasswordRegex = re.compile(r'.{8,}')
hasUpperRegex = re.compile(r'[A-Z]+')
hasLowerRegex = re.compile(r'[a-z]+')
hasDigitRegex = re.compile(r'\d+')

isPasswordStrong = False

while not isPasswordStrong:

    print('Please input your password:')
    password = input()

    mo1 = longPasswordRegex.search(password)
    mo2 = hasUpperRegex.search(password)
    mo3 = hasLowerRegex.search(password)
    mo4 = hasDigitRegex.search(password)

    if mo1 == None or mo2 == None or mo3 == None or mo4 == None:
        print('Your password is not strong enough. Try another one.')
    else:
        isPasswordStrong = True
        print('Your password is strong enough.')
