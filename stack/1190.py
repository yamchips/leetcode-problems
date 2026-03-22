def reverseParentheses(s: str) -> str:
    stack = []
    res = ""
    for char in s:
        if char == "(":
            stack.append(res)
            res = ""
        elif char == ")":
            res = res[::-1]
            res = stack.pop() + res
        else:
            res += char
    return res