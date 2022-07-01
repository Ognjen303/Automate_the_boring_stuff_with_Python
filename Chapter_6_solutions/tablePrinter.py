def printTable(tableData):
    '''Write a function named printTable() that takes a list of lists of strings
    and displays it in a well-organized table with each column right-justified.
    Assume that all the inner lists will contain the same number of strings. '''

    colWidths = [0] * len(tableData)
    for i in range(len(tableData)): # loop over rows of tableData
        for word in tableData[i]:
            if len(word) > colWidths[i]:
                colWidths[i] = len(word)

    for j in range(len(tableData[0])): # loop over columns of tableData
        line = []
        for i in range(len(tableData)): # loop over rows of tableData
                line.append(tableData[i][j].rjust(colWidths[i]))
        print(' '.join(line))


tableData = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Koko', 'Carol', 'David'],
         ['dogs', 'cats', 'Ognie', 'goose']]

printTable(tableData)
