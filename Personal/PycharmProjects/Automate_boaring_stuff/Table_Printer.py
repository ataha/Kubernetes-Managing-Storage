
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)

    for i in range(len(table)):
        colWidths[i] = len(max(table[i], key=len))

    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].rjust(colWidths[item]), end=' ')
        print()

printTable(tableData)