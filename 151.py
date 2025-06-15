def reverseWords(s:str) -> str:
    stack = []
    word = ''
    s += ' '
    for i in range(len(s)):      
        if s[i] != ' ':
            word += s[i]
        else:
            if word:
                stack.append(word)
                word = ''
    res = ''
    while stack:
        res += stack.pop() + ' '
    return res.strip()

def reverseWords2(s:str)->str:
    words = s.split()
    words.reverse()
    res = ''
    for word in words:
        res += word + ' '
    return res.strip() 


if __name__=='__main__':
    print(reverseWords('the  sky is blue'))
    print(reverseWords('  hello  world  '))