def setZeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    rows = set()
    cols = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    # deal with each zero element
    while rows:
        row = rows.pop()
        matrix[row][:] = [0] * n
    while cols:
        col = cols.pop()
        for i in range(m):
            matrix[i][col] = 0

def setZeroes2(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    firstColZero = False
    for i in range(m):
        if matrix[i][0] == 0:
            firstColZero = True
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        if matrix[i][0] == 0:
            matrix[i][:] = [0] * n
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        matrix[0][:] = [0] * n
        for i in range(m):
            matrix[i][0] = 0
    if firstColZero:
        for i in range(m):
            matrix[i][0] = 0


if __name__=='__main__':
    (setZeroes2([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    setZeroes2([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])
    