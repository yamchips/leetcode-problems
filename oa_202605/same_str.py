import re

def solution(first, second):
    words1 = set(re.findall(r"[A-Za-z]+", first))
    words2 = set(re.findall(r"[A-Za-z]+", second))
    return len(words1 & words2)

if __name__=="__main__":
    case1 = ("Yes, we all really like pizza.", "Where can we buy pizza around here?")
    case2 = ("There were four people at dinner.", "There were seven people at dinner.")
    case3 = ("", "")
    outputs = [solution(case1[0], case1[1]),
               solution(case2[0], case2[1]),
               solution(case3[0], case3[1])]
    print(outputs) # should be [2, 5, 0]