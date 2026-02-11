from collections import Counter


def frequencySort(s: str) -> str:
    freq = Counter(s)
    buckets = [[] for _ in range(len(s) + 1)]
    for key, count in freq.items():
        buckets[count].append(key)
    res = []
    for i in range(len(buckets) - 1, 0, -1):
        if buckets[i]:
            for char in buckets[i]:
                for _ in range(i):
                    res.extend(char)
    result = ''
    for char in res:
        result += char
    return result

def frequencySort(s: str) -> str:
    freq = Counter(s)
    buckets = [[] for _ in range(len(s) + 1)]
    for key, count in freq.items():
        buckets[count].append(key)
    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for char in buckets[i]:
            res.append(char*i)
    return ''.join(res)

def frequencySort(s: str) -> str:
    freq = Counter(s)
    newFreq = sorted(freq.items(), key = lambda x : x[1], reverse=True)
    res = []
    for char, count in newFreq:
        res.append(char * count)
    return ''.join(res)


if __name__=="__main__":
    frequencySort('tree')