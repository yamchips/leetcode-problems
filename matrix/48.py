def rotate1(matrix: list[list[int]]) -> None:
    n = len(matrix)
    seen = set()
    for i in range(n):
        for j in range(n):
            if (i,j) not in seen:
                temp = matrix[i][j]

                matrix[j][n - 1 - i], temp = temp, matrix[j][n - 1 - i]
                seen.add((i, j))
                                
                matrix[n - 1 - i][n - 1 - j], temp = temp, matrix[n - 1 - i][n - 1 - j]
                seen.add((j, n - 1 - i))
                                
                matrix[n- 1 - j][i], temp = temp, matrix[n- 1 - j][i]
                seen.add((n - 1 - i, n - 1 - j))
                                    
                matrix[i][j], temp = temp, matrix[i][j]
                seen.add((n - 1 - j, i))
                if len(seen) == n * n:
                    print(matrix)
                    return
                
def rotate2(matrix: list[list[int]]) -> None:
    n = len(matrix)
    # transpose the matrix

    # swap each column

def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    # reverse the matrix, 1st row to last
    matrix.reverse()
    # transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)

if __name__=='__main__':
    rotate([[1,2,3],[4,5,6],[7,8,9]])
    rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
    