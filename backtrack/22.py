def generateParenthesis(n: int) -> list[str]:
    res = []
    backtrack(res, [], n, 0, 0)
    return res

def backtrack(res:list[list[str]], temp:list[str], n:int, left: int, right: int) -> None:
    if len(temp) == 2 * n:
        res.append(''.join(temp))
        return
    
    if left < n:
        temp.append('(')
        left += 1
        backtrack(res, temp, n, left, right)
        temp.pop(-1)
        left -= 1
    if right < left:
        temp.append(')')
        right += 1 
        backtrack(res, temp, n, left, right)   
        temp.pop(-1)
        right -= 1

if __name__=='__main__':
    print(generateParenthesis(3))