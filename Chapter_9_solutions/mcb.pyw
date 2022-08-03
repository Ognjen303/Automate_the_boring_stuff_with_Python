#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: mcb.bat save <keyword> - Saves clipboard to keyword.
#        mcb.bat <keyword> - Loads keyword to clipboard.
#        mcb.bat list - Loads all keywords to clipboard.
#        mcb.bat delete <keyword> - Deletes keyword from shelf.
#        mcb.bat delete - Deletes all entries.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3:

    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1].lower() == 'delete':
        # Delete keyword from shelf
        del mcbShelf[sys.argv[2]]


elif len(sys.argv) == 2:
    # List keywords, load content, or delete all content.

    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sysargv[1].lower() == 'deleteall':
        # mcbShelf.clear()
        for keyword in list(mcb_shelf.keys()):
            del mcbShelf[keyword]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])



mcbShelf.close()
