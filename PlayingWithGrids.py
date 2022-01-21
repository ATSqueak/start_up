'''
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

'''

'''
print('Printing a grid')
print()
print()

for x in range(8):
    for y in range(5):
        print(x,y)

nums = []
for i in range(4):
    nums.append([])
    for j in range(1, 4):
        nums[i].append(j)
print("grid with numbers:")
print(nums)


'''

'''
def print_grid(grid):
    for row in grid:
        print(" ".join(row))



grid = []

for x in range(0, 5):
    grid.append(["O"] * 5)
print(grid)

print_grid(grid)

'''

print('Grid')
print()
for x in range(0, 3):
    print()
    for y in range(0, 3):
        print('X', end=' ')
print()

grid = [['.', '.', '0','0','.', '0', '0','.', '.'],
        ['.', 'O', 'O', '0', '0','0','0','0', '.'],
        ['.', 'O', 'O', '0', '0','0','0','0', '.'],
        ['.', '.', 'O', '0', '0','0','0','.', '.'],
        ['.', '.', '.', '0', '0','0','.','.', '.'],
        ['.', '.', '.', '.', '0','.','.','.', '.'],
]

for x in range(len(grid)):
    print()
    for y in range(len(grid[x])):
        print(grid[x][y],end='')

