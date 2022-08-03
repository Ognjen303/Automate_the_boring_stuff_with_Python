#! python3

# Write a program that walks through a folder tree and searches for excep
# tionally large files or folders—say, ones that have a file size of more than
# 100MB. (Remember that to get a file’s size, you can use os.path.getsize() from
# the os module.) Print these files with their absolute path to the screen.

from pathlib import Path
import os

# TODO: For a given folder,
# search all for all files or subfolders with size over 100MB

folder = Path('C:\\')

# limit is 100MB = 1e8 bytes
sizeLimit = 1e8

for foldername, subfolders, filenames in os.walk(folder):

    folderSize = os.path.getsize(Path(foldername))
    if folderSize >= sizeLimit:
        print(f'size: {round(1.0 * folderSize / 1e6, 2)} MB, {foldername} ')

    for filename in filenames:

        filenameAbsPath = Path(foldername) / filename
        fileSize = os.path.getsize(filenameAbsPath)

        if fileSize >= sizeLimit:
            print(f'size: {round(1.0 * fileSize / 1e6, 2)} MB, {filenameAbsPath}')

print('Done.')

