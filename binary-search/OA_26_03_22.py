import bisect


def solution1(diff):
    rating = 1500
    max_val = 1500
    for num in diff:
        rating += num
        if rating > max_val:
            max_val = rating
    return [max_val, rating]

def solution2(text):
    vowels = set("aeiouAEIOU")
    result = []
    for word in text:
        if len(word) > 1 and word[0] in vowels and word[-1] in vowels:
            temp = word[1:-1][::-1]
            result.append(word[0] + temp + word[-1])
        else:
            result.append(word)
    return result  

def solution3(puzzle):
    rows, cols = len(puzzle), len(puzzle[0])
    max_val = float("-inf")
    symbols = set("+-")
    for row in range(rows):
        for col in range(cols):
            if puzzle[row][col] in symbols:
                continue
            start_val = int(puzzle[row][col])
            max_val = max(max_val, start_val)
            for dx, dy in [(1,0), (0,1)]:
                x, y = row, col
                expect_operator = True
                current = start_val

                while True:
                    x += dx
                    y += dy
                    if not (0 <= x < rows and 0 <= y < cols):
                        break
                    val = puzzle[x][y]
                    if expect_operator:
                        if val not in symbols:
                            break
                        last_operator = val
                        expect_operator = False
                    else:
                        if not ('0' <= val <= '9'):
                            break
                        num = int(val)
                        if last_operator == "+":
                            current += num
                        else:
                            current -= num
                        max_val = max(current, max_val)
                        expect_operator = True
    return max_val


def solution4(heights, viewingGap):
    n = len(heights)
    seen = []
    result = float("inf")
    for i in range(viewingGap, n):
        bisect.insort(seen, heights[i - viewingGap])
        h = heights[i]
        index = bisect.bisect_left(seen, h)
        if index < len(seen):
            result = min(result, abs(h - seen[index]))
        if index > 0:
            result = min(result, abs(h - seen[i - 1]))
        if result == 0:
            return 0
    return result
