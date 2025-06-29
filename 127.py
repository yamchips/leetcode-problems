from collections import deque


def diff(word1: str, word2: str) -> int:
    # return the number of different digits
    # assume word1.length = word2.length
    res = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            res += 1
    return res

# the feasible path can jump back and forth in the sorted list
def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord not in wordList: return 0
    wordList.sort()
    endIndex = wordList.index(endWord)
    leftBegin, rightBegin = -1, len(wordList) + 1
    for index, word in enumerate(wordList):
        if diff(word, beginWord) == 1 or diff(word, beginWord) == 0:
            if index < endIndex:
                leftBegin = max(leftBegin, index)
            else:
                rightBegin = min(rightBegin, index)
    if leftBegin == -1 and rightBegin == len(wordList) + 1:
        return 0
    leftCount, rightCount = -1, -1
    if leftBegin >= 0:
        reach = True
        for i in range(leftBegin, endIndex):
            if diff(wordList[i], wordList[i + 1]) == 1:
                continue
            else:
                reach = False
                break
        if reach:
            leftCount = endIndex - leftBegin + 1
    if rightBegin != len(wordList) + 1:
        reach = True
        for i in range(endIndex, rightBegin):
            if diff(wordList[i], wordList[i + 1]) == 1:
                continue
            else:
                reach = False
                break
        if reach:
            rightCount = rightBegin - endIndex + 1
    if leftCount == -1 and rightCount == -1:
        return 0
    if leftCount == -1:
        if wordList[rightBegin] != beginWord:
            return rightCount + 1
        else:
            return rightCount
    if rightCount == -1:
        if wordList[leftBegin] != beginWord:
            return leftCount + 1
        else:
            return leftCount
    if leftCount != -1 and leftCount < rightCount:
        if wordList[leftBegin] != beginWord:
            return leftCount + 1
        else:
            return leftCount
    if rightCount != -1 and rightCount < leftCount:
        if wordList[rightBegin] != beginWord:
            return rightCount + 1
        else:
            return rightCount

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
