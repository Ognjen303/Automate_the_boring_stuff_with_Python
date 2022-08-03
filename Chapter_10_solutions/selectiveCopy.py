#! python3
# Write a program that walks through a folder tree and searches for files with
# a certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder.

from pathlib import Path
import os, shutil, re

# Change path to something suitable on your computer
folder = Path('C:/Fizicki fakiltet')



# Regex to search for .pdf files, change to something else if you want to, like .txt, .jpg etc...
filenameRegex = re.compile(r'.*(\.pdf)$')

def selectiveCopy(folder):
    '''New folder location is in subfolder of "folder". '''


    if not os.path.exists(folder):
        print(f'The folderpath {folder} does not exists. Check your input.')
        return None

    folder = Path(os.path.abspath(folder))

    destFolder = folder / 'pdf_files'
    if not os.path.exists(destFolder):
        # Check if destination directory exists, if not create it
        os.makedirs(destFolder)

    for foldername, subfolders, filenames in os.walk(folder):


        for filename in filenames:

            # --------------------- NOTE --------------
            # easier to use istead of a Regex is
            # if filename.endswith('.pdf'):
            #       do stuff...
            mo = filenameRegex.search(filename)

            # If we found a .pdf file and it is not already copied to
            # the destination folder, copy the .pdf file
            if mo is not None and not os.path.exists(destFolder / mo.group()):
                print(f'File copied {mo.group()} into destination folder {destFolder}\n')
                shutil.copy(Path(foldername) / mo.group(), destFolder)

    print('Done copying files.')
    return None

selectiveCopy(folder)
