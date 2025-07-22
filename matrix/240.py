def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    def searchRow(row, target):
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] < target:
                left = mid + 1
            elif row[mid] > target:
                right = mid - 1
            else:
                return True
        return False
    for row in matrix:
        if row[0] <= target <= row[-1]:
            res = searchRow(row, target)
            if res:
                return True
    return False

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    def compare(matrix, target, row, col, m, n):
        if row >= m or col < 0:
            return False
        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            return compare(matrix, target, row + 1, col, m, n)
        else:
            return compare(matrix, target, row , col - 1, m, n)
    return compare(matrix, target, 0, n - 1, m, n)

if __name__=='__main__':
    print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 7)) # expected true
    print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)) # expected false
    print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24]], 20)) # expected false
    print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]], 1)) # expected true
