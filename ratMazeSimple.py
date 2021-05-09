
def ratMaze(board, solution: list):
    x, y = solution[-1]
    if x == len(board) - 1 and y == len(board[0]) - 1:
        return solution
    if y + 1 < len(board[0]) and board[x][y + 1] == 1:
        solution.append((x, y + 1))
        ans = ratMaze(board, solution)
        if ans:
            return ans
        else:
            solution.pop()
    if x + 1 < len(board[0]) and board[x + 1][y] == 1:
        solution.append((x + 1, y))
        ans = ratMaze(board, solution)
        if ans:
            return ans
        else:
            solution.pop()
    return None
def printSoln(solution):
    rows, cols = solution[-1]
    solution = set(solution)
    for i in range(rows + 1):
        for j in range(cols + 1):
            if (i, j) in solution:
                print(1, end = " ")
            else:
                print(0, end = " ")
        print()




board = [[1,0,0,0], [1, 0, 0, 1], [0,1,0,0], [1,1,1,1]]

solution = ratMaze(board, [(0,0)])
printSoln(solution)