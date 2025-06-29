from collections import deque


def diff(word1: str, word2: str) -> int:
    # return the number of different digits
    # assume word1.length = word2.length
    res = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            res += 1
    return res

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    queue = deque([beginWord])
    length = 1
    while queue:
        size = len(queue)
        for _ in range(size):
            current = queue.popleft()
            if current == endWord:
                return length
            added = []
            for word in wordSet:
                if diff(word, current) == 1:
                    queue.append(word)
                    added.append(word)
            for element in added:
                wordSet.remove(element)
        length += 1
    return 0
    



if __name__=='__main__':
    print(ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])) # 5
    print(ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"])) # 0
    print(ladderLength('hot', 'dog', ['hot', 'dog']))
