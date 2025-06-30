from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    countMap = defaultdict(int)
    def checkBoard(board: list[list[str]], row:int, col:int)-> bool:
        item = board[row][col]
        if item != '.':
            countMap[item] += 1
            if countMap[item] > 1:
                return False
        return True
    res = True
    # check each row
    for row in range(9):
        for col in range(9):
            res = checkBoard(board, row, col)
            if not res:
                return False
        countMap.clear()
    # check each column
    for col in range(9):
        for row in range(9):
            res = checkBoard(board, row, col)
            if not res:
                return False
        countMap.clear()
    # check each 3*3 grid
    indices = [(0,3,0,3),
               (0,3,3,6),
               (0,3,6,9),
               (3,6,0,3),
               (3,6,3,6),
               (3,6,6,9),
               (6,9,0,3),
               (6,9,3,6),
               (6,9,6,9)
               ]
    for row1, row2, col1, col2 in indices:
        for row in range(row1, row2):
            for col in range(col1, col2):
                res = checkBoard(board, row, col)
                if not res:
                    return False
        countMap.clear()
    return True

def isValidSudoku(board: list[list[str]]) -> bool:
    elements = set()
    for row in range(9):
        for col in range(9):
            item = board[row][col]
            box = (row // 3, col // 3)
            if item != '.':
                if ((item, 'row', row) in elements or 
                    (item, 'col', col) in elements or 
                    (item, 'box', box) in elements):
                    return False
                elements.add((item, 'row', row))
                elements.add((item, 'col', col))
                elements.add((item, 'box', box))
    return True

        
if __name__=='__main__':
    print(isValidSudoku([
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    #print(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    # print(isValidSudoku(
    #     [[".","2",".",".",".",".",".",".","."],
    #      [".",".",".",".",".",".","5",".","1"],
    #      [".",".",".",".",".",".","8","1","3"],
    #      ["4",".","9",".",".",".",".",".","."],
    #      [".",".",".",".",".",".",".",".","."],
    #      [".",".","2",".",".",".",".",".","."],
    #      ["7",".","6",".",".",".",".",".","."],
    #      ["9",".",".",".",".","4",".",".","."],
    #      [".",".",".",".",".",".",".",".","."]]))