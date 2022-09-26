#! python3

import openpyxl
from pathlib import Path

# Path that contains the desired .txt files
# change to whatever is suitable for you
p = Path(r'C:\automate the boring stuff fajlovi\automate_online-materials')

listOfTextFiles = list(p.glob('*.txt'))

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, len(listOfTextFiles) - 1):
    file = open(listOfTextFiles[i - 1], 'r')
    fileContent = file.readlines()

    for j in range(1, len(fileContent) + 1):
        sheet.cell(row = j, column = i).value = str(fileContent[j - 1])

    file.close()
wb.save('textToSheet.xlsx')
wb.close
