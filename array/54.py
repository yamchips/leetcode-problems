def spiralOrder1(matrix: list[list[int]]) -> list[int]:
    result = []
    def deleteFr(matrix: list[list[int]], result:list):
        result.extend(matrix.pop(0))
    def deleteLc(matrix: list[list[int]], result:list):
        for row in matrix:
            result.append(row.pop(-1))
        matrix[:] = [row for row in matrix if row]
    def deleteLr(matrix: list[list[int]], result:list):
        # reverse modify list in-place, [::-1] create a shallow copy
        result.extend(matrix.pop(-1)[::-1]) 
    def deleteFc(matrix: list[list[int]], result:list):
        fc = []
        for row in matrix:
            fc.append(row.pop(0))
        matrix[:] = [row for row in matrix if row]
        fc.reverse()
        result.extend(fc)
    while matrix: 
        deleteFr(matrix, result)
        if not matrix:
            return result
        deleteLc(matrix, result)
        if not matrix:
            return result
        deleteLr(matrix, result)
        if not matrix:
            return result
        deleteFc(matrix, result)
        if not matrix:
            return result
    return result

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m = len(matrix)
    n = len(matrix[0])
    left, right, top, bottom = 0, n, 0, m
    result = []
    while left < right and top < bottom:
        
        row = top
        for col in range(left, right):
            result.append(matrix[row][col])
        top += 1

        col = right - 1
        for row in range(top, bottom):
            result.append(matrix[row][col])
        right -= 1

        if top < bottom:
            row = bottom - 1
            for col in range(right - 1, left - 1, -1):
                result.append(matrix[row][col])
            bottom -= 1

        if left < right:
            col = left
            for row in range(bottom - 1, top - 1, -1):
                result.append(matrix[row][col])
            left += 1


    return result

if __name__=='__main__':
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(spiralOrder([[8],[9],[0]]))