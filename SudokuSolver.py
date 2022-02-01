COLS = ROWS = 9
cols = [set() for _ in range(COLS)]
rows = [set() for _ in range(ROWS)]
subgrids = {grid:set() for grid in range(1, ROWS + 1)}
def preScan(grid):
    for i in range(ROWS):
        for j in range(COLS):
            ele = grid[i][j]
            if ele != 0:
                rows[i].add(ele)
                cols[j].add(ele)
                subgrids[getSubGridNumber(i, j)].add(ele)
def isSafe(i, j, number):
    return (number not in rows[i]) and (number not in cols[j]) and (number not in subgrids[getSubGridNumber(i, j)])
def getNext(row, col, grid):
    while row < ROWS:
        while col < COLS:
            if grid[row][col] == 0:
                return (row, col)
            col += 1
        col = 0
        row += 1
    return row, col
def solveSudoku(row, col, grid):
    if row >= ROWS:
        return True
    else:
        gridNum = getSubGridNumber(row, col)

        for i in range(1, ROWS + 1):
            if isSafe(row, col, i):
                grid[row][col] = i
                rows[row].add(i)
                cols[col].add(i)

                subgrids[gridNum].add(i)
                nextRow, nextCol = getNext(row, col, grid)
                ans = solveSudoku(nextRow, nextCol, grid)
                if ans: return ans
                grid[row][col] = 0
                rows[row].remove(i)
                cols[col].remove(i)
                subgrids[gridNum].remove(i)
        return False



def getSubGridNumber(i, j):
    vertical = j // 3
    horizontal = i // 3
    gridNumber = horizontal * 3 + (vertical + 1)
    return gridNumber
grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]
preScan(grid)
solveSudoku(*getNext(0, 0, grid), grid)
for row in grid:
    print(row)