def isValid(s: str) -> bool:
    stack = []
    dict = {'[':']', '(':')', '{':'}'}
    for char in s:
        if char == '[' or char == '(' or char == '{':
            stack.append(dict[char])
        else:
            if stack:
                p = stack.pop()
                if p != char:
                    return False
            else:
                return False
    return len(stack) == 0

def isValid(s: str) -> bool:
    stack = []
    pairs = {'[':']', '(':')', '{':'}'}
    for char in s:
        if char in pairs:
            stack.append(pairs[char])
        elif not stack or stack.pop() != char:
            return False
    return not stack