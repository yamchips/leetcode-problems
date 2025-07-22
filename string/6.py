def convert(s:str, num:int) -> str:
    if num == 1 or num > len(s): return s
    rows = [[] for _ in range(num)]
    
    cycleLen = 2 * num - 2
    for i in range(len(s)):
        position = i % cycleLen
        if position < num:
            rows[position].append(s[i])
        else:
            rows[cycleLen-position].append(s[i])
    result = ''.join([''.join(row) for row in rows])
    return result

# string concatenation slows down the running time
def convert2(s:str, num:int) -> str:
    if num > len(s) or num == 1: return s
    rows = [''] * num
    
    cycleLen = 2 * num - 2
    for i in range(len(s)):
        position = i % cycleLen
        if position < num:
            rows[position] += (s[i])
        else:
            rows[cycleLen-position] += s[i]
    result = ''
    for row in rows:
        result+=row
    return result

def convert3(s:str, n:int) -> str:
    if n > len(s) or n == 1: return s
    rows = [[] for _ in range(n)]
    index = 0
    direction = 1
    for i in range(len(s)):
        rows[index].append(s[i])
        if index == n - 1:
            direction = -1
        if index == 0:
            direction = 1
        index += direction
    result = []
    for row in rows:
        result.append(''.join(row))
    return ''.join(result)


if __name__=='__main__':
    print(convert3('PAYPALISHIRING', 3))
    print(convert3('PAYPALISHIRING', 4))
    print(convert3('A', 4))
    

