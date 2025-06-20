# O(n) space, O(n) time
def wordDistance(words: list[str], word1: str, word2: str) -> int:
    indices = []
    for i, word in enumerate(words):
        if word == word1:
            indices.append((i, 0))
        elif word == word2:
            indices.append((i, 1))
    minDistance = len(words)
    for i in range(len(indices) - 1):
        if indices[i][1] != indices[i + 1][1]:
            minDistance = min(minDistance, indices[i+1][0]-indices[i][0])
    return minDistance

def wordDistance(words: list[str], word1: str, word2: str) -> int:
    index1, index2 = -1, -1
    minDistance = len(words)
    for i, word in enumerate(words):
        if word == word1:
            index1 = i
        elif word == word2:
            index2 = i
        if index1 >= 0 and index2 >= 0:
            minDistance = min(minDistance, abs(index1- index2))       
    return minDistance

if __name__=='__main__':
    # expected 3
    print(wordDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice')) 

    # expected 1
    print(wordDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'makes'))

    # expected 1
    print(wordDistance(['a', 'b', 'a'], 'a', 'b')) 
