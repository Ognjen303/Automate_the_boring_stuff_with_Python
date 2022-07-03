import re

def regex_strip(s, chars = None):

    if chars:
        trim = '[' + re.escape(chars) + ']*'
    else:
        trim = r'\s*'

    return re.fullmatch(f"{trim}(.*?){trim}", s).group(1)

print(regex_strip('   Hello, world    ', ' '))
