#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

# sys gives us access to .argv
# sys.argv first agrument is name of program

if len(sys.argv) > 1:
    # Get adress from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get adress from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
