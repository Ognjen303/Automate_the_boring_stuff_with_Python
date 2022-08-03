# Code assumes that the madLibs.py and madLibs.txt are in same folder
# Mad Libs program that reads in text files and lets the user add
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file


from pathlib import Path
import pyinputplus as pyip
import re


# open file in read mode

textFile = open(Path.cwd() / 'madLibs.txt', 'r')

textContent = textFile.read()
textFile.close()

wordSwapRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

toSwap = wordSwapRegex.findall(textContent)

# toSwap is of type tuple
print(toSwap)

for x in toSwap:
    response = pyip.inputStr(prompt='Enter an ' + x + ':\n')
    textContent = textContent.replace(x, response, 1)

# Write to outputFile
outputFile = open(Path.cwd() / 'madLibsEdited.txt', 'w')
outputFile.write(textContent)
print(textContent)
outputFile.close()
