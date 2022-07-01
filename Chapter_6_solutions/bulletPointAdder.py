#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the starts
# of each line of the on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

# pyperclip.copy() returns a string
pyperclip.copy(text)
