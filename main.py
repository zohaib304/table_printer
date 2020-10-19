tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['alice', 'bod', 'carol', 'david'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):

    rows = len(tableData[0])
    columns = len(tableData)

    column_widths = [max(len(cell) for cell in column) for column in table]

    print_row = ["" for i in range(rows)]
    for row in range(rows):
        print_row[row] = ' '.join(
            table[col][row].rjust(column_widths[col])
            for col in range(columns)
        )

    for item in print_row:
        print(item)


printTable(tableData)
