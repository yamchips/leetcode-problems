'''
Given a matrix of 0, 1, 2, return the length of longest diagnol that fits this pattern: 1, 2, 0, 2, 0, 2, 0...
First number is 1, then 2 and 0 appear alternately. When we reach the border of the matrix, the count stops. If the pattern breaks in the middle, we don't count the length.

Example 1:
[[0, 0, 1, 2],
 [0, 2, 2, 2],
 [2, 1, 0, 1]]
the max length is three, starting from bottom right 1 and go left up.

Example 2:
[[1, 1, 1, 1, 1, 0],
 [1, 2, 1, 1, 2, 1],
 [1, 1, 0, 1, 1, 1],
 [1, 1, 2, 2, 1, 1],
 [1, 0, 1, 1, 0, 1],
 [2, 1, 1, 1, 1, 1]]
the max length is four, starting from 4th 1 in row 3 and go left down.
'''

def longest_pattern(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
    maxLength = 0

    def checkPattern(x, y, dx, dy):
        expected = 2
        length = 1
        row, col = x + dx, y + dy
        toggle = True
        while 0 <= row < rows and 0 <= col < cols:
            if matrix[row][col] != expected:
                length = 1
                break
            length += 1
            expected = 0 if toggle else 2
            toggle = not toggle
            row += dx
            col += dy
        return length
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                for dx, dy in directions:
                    maxLength = max(maxLength, checkPattern(i, j, dx, dy))
    return maxLength