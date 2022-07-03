import re

def ifValidDate(day, month, year):
    '''Returns if the entered date is valid'''
    if int(year) < 1000 or int(year) > 2999:
        return False

    if int(month) > 12 or int(month) < 1:
        return False

    if month in ['04', '06', '09', '11']: # month has 30 days
        if int(day) < 1 or int(day) > 30:
           return False
    elif month in ['01', '03', '05', '07', '08', '10', '12']:
        if int(day) < 1 or int(day) > 31:
           return False
    elif month == '02':
        if int(day) < 1 or int(day) > 29:
            return False
        elif day == '29':
            if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0: # check if year is leap
                return True
            else: # not a leap year
                return False


    return True

dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')

mo = dateRegex.search('This is a sentence, the date is 29/02/1800.')

if(mo == None):
    print('These is no date in the sentence.')
else:
    day, month, year = mo.group(1), mo.group(2), mo.group(3)

    validDate = ifValidDate(day, month, year)
    print(f'The date entered is valid: {validDate}')





