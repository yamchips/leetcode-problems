def simplifyPath1(path: str) -> str:
    stack = []
    n = len(path)
    curr = ''
    for i, char in enumerate(path):
        if i == n - 1:
            if char == '.':
                if curr == '.':
                    if stack:
                        stack.pop()
                else:
                    if curr != '':
                        stack.append(curr + char)
            elif char == '/':
                if curr != '.' and curr != '..' and curr != '':
                    stack.append(curr)
            else:
                stack.append(curr + char)
            break
        if char == '/' :
            if curr == '..':
                if stack:
                    stack.pop()
            elif curr != '.' and curr != '':
                stack.append(curr)
            curr = ''
            continue    
        curr += char
    res = '/'.join(stack)
    return '/'+res if len(res) > 0 else '/'

def simplifyPath(path: str) -> str:
    content = path.split('/')
    stack = []
    for char in content:
        if char != '':
            if char != '..' and char != '.':
                stack.append(char)
            elif char == '..' and stack:
                stack.pop()      
    return '/' + '/'.join(stack)

if __name__=='__main__':
    print(simplifyPath('/.'))
    print(simplifyPath("/..."))
    print(simplifyPath("/a//../../b/../c//.//"))
    print(simplifyPath('/.../a/../b/c/../d/./'))
    print(simplifyPath('/../'))
    print(simplifyPath('/home/user/Documents/../Pictures'))
    print(simplifyPath('/home//foo/'))
    print(simplifyPath('/home/'))
    print(simplifyPath('/a//b////c/d//././/..'))
