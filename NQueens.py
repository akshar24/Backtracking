diagonal1 = set()
diagonal2 = set()
rows = set()
def isSafe(i, j):
    return (not (i + j) in diagonal1) and (not (i - j) in diagonal2) and (not i in rows)
def place(solution, col, N):
    if col >= N:
        soln = list()
        for i in range(N):
            row = ""
            for j in range(N):
                if (i, j) in solution:
                    row += "Q"
                else:
                    row += "."
            soln.append(row)
        for row in soln:
            print(row)
        print()
        return
    for row in range(N):
        if isSafe(row, col):
            rows.add(row)
            diagonal2.add(row - col)
            diagonal1.add(row + col)
            solution.append((row, col))
            place(solution, col + 1, N)

            rows.remove(row)
            diagonal2.remove(row - col)
            diagonal1.remove(row + col)
            solution.pop()
    return None
def printSolution(solution, N):
    solution = set(solution)
    for i in range(N):
        for j in range(N):
            if (i, j) in solution:
                print(1, end = " ")
            else:
                print(0, end  = " ")
        print()

N=9
solution = place(list(), 0, N)