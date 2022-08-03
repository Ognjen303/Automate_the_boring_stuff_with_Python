#! python3
# renameDates.py - Renames the filenames with American MM-DD-YYYY date format
# to European style DD-MM-YYYY

import shutil, re, os

# Create Regexes that match files with the American date format.
# re.VERBOSE dozvoljava da lakse vizuelno vidim koji Regex kucam

datePattern = re.compile(r"""^(.*?) # all text before the date
            ((0|1)?\d)-     # one or two digits for the month
            ((0|1|2|3)?\d)-     # one or two digits for the day
            ((19|20)\d\d)   # four digits for the year
            (.*?)$          # all text after the date
            """, re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir('.'): # '.' represents current working directory
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)


    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart


    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    # shutil.move(amerFilename, euroFilename) # uncomment after testing
