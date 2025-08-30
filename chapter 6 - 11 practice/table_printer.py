def printTable(tableData: list[list[str]]) -> None:
    colWidth = [max(len(item) for item in col) for col in tableData]
#This should give 3 lengths of the longest string in the column


    tableColumn = len(tableData)
    tableRow = len(tableData[0])
    for row in range(tableRow):
        for column in range(tableColumn):
            print(str(tableData[column][row]).rjust(colWidth[column]), end= " ")
        print()


