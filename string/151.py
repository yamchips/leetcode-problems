import re

def reverseWords(s: str) -> str:
    word = ""
    word_list = []
    s = s.strip()
    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                word_list.append(word)
            word = ""
    word_list.append(word)
    return " ".join(word_list[::-1])

def reverseWords(s: str) -> str:
    result = re.findall(r"[A-Za-z0-9]+", s)
    result.reverse()
    return " ".join(result)