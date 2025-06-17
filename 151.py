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

# use list to simulate a mutable string
def reverseWords3(s: str) -> str:
    s = list(s)
    s.reverse()
    startIndex, n = 0, len(s)
    endIndex = 0
    while startIndex < n:
        while startIndex < n and s[startIndex] == ' ':
            startIndex += 1
        if startIndex != n and endIndex > 0:
            s[endIndex] = ' '
            endIndex += 1

        wordStart = endIndex  # Save start of current word

        while startIndex < n and s[startIndex] != ' ':
            s[endIndex] = s[startIndex]
            startIndex += 1
            endIndex += 1

        reverse(s, wordStart, endIndex - 1)

    s = s[:endIndex]
    return ''.join(s)


def reverse(s:list, left:int, right:int)->None:
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__=='__main__':
    # print(reverseWords3(' the  sky is blue '))
    print(reverseWords3('  hello  world  '))