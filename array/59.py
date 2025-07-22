def generateMatrix(n: int) -> list[list[int]]:
    result = [[0] * n for _ in range(n)]
    nums = []
    for i in range(1, n**2 + 1):
        nums.append(i)

    left, right, top, bottom = 0, n, 0, n
    while left < right and top < bottom:

        row = top
        for col in range(left, right):
            result[row][col] = nums.pop(0)
        top += 1

        col = right - 1
        for row in range(top, bottom):
            result[row][col] = nums.pop(0)
        right -= 1

        if top < bottom:
            row = bottom - 1
            for col in range(right - 1, left - 1, -1):
                result[row][col] = nums.pop(0)
            bottom -= 1

        if left < right:
            col = left
            for row in range(bottom - 1, top - 1, -1):
                result[row][col] = nums.pop(0)
            left += 1
    
    return result

if __name__=='__main__':
    print(generateMatrix(3))
    print(generateMatrix(4))