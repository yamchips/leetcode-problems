import re

def solution(first, second):
    words1 = set(re.findall(r"[A-Za-z]+", first))
    words2 = set(re.findall(r"[A-Za-z]+", second))
    return len(words1 & words2)

def is_letter(input):
    return 'a' <= input <= 'z' or 'A' <= input <= 'Z'

def get_words(input):
    words = set()
    left, right = 0, 0
    while right < len(input):
        # move left to letter
        while left < len(input) and not is_letter(input[left]):
            left += 1
        # move right to non-letter
        right = left
        while right < len(input) and is_letter(input[right]):
            right += 1
        if left < right:
            words.add(input[left:right])
        # move left to right
        left = right
    return words

def solution(first, second):
    first_words = get_words(first)
    print(first_words)
    second_words = get_words(second)
    return len(first_words & second_words)

if __name__=="__main__":
    case1 = ("Yes, we all really like pizza.", "Where can we buy pizza around here?")
    case2 = ("There were four people at dinner.", "There were seven people at dinner.")
    case3 = ("", "")
    outputs = [solution(case1[0], case1[1]),
               solution(case2[0], case2[1]),
               solution(case3[0], case3[1])]
    print(outputs) # should be [2, 5, 0]