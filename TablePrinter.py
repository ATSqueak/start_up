'''
Table Printer
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:
             tableData = [['apples', 'oranges', 'cherries', 'banana'],
                          ['Alice', 'Bob', 'Carol', 'David'],
                          ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:
                apples Alice  dogs
               oranges   Bob  cats
              cherries Carol moose
                banana David goose
Hint: Your code will first have to find the longest string in each of the inner lists so that the whole column can be wide enough to fit all the strings.
You can store the maximum width of each column as a list of integers. The printTable() function can begin with colWidths = [0] * len(tableData),
which will create a list containing the same number of 0 values as the number
of inner lists in tableData. That way, colWidths[0] can store the width of the longest string in tableData[0],
colWidths[1] can store the width of the longest string in tableData[1], and so on.
You can then find the largest value in the colWidths list to find out what integer width to pass to the rjust() string method.
'''

def printTable(inputList):
    # initialize the list "colWidths" with zeroes equal to the length of the input list
    colWidths = [0] * len(inputList)

    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if len(inputList[i][j]) > colWidths[i]:
                colWidths[i] = len(inputList[i][j])
    #print(colWidths)
    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    # in colWidths
    for x in range(len(inputList[0])):
        for y in range(len(inputList)):
            print(inputList[y][x].rjust(colWidths[y]), end=' ')
        print()

print('Table Printer Program')
tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

colWidths = [0] * len(tableData)
#print(colWidths)
print('**********************')
outer = len(tableData)
print('How many outer items in the list ' + str(outer))

for i in range(len(tableData)):
    inner = len(tableData[i])
print('How many items in the inner list ' + str(inner))
print('**********************')

for i in range(len(tableData)):
    #print(tableData[i])
    for y in range(len(tableData[i])):
        #print(tableData[i][y])
        if colWidths[i] < len(tableData[i][y]):
            colWidths[i] = len(tableData[i][y])
#print(colWidths)


# for h in tableData:
#    print(h)

# for l in tableData:
#    for x in l:
#        print(x)

# print(len(max(tableData, key=len)))
# print(len(max(tableData)))



