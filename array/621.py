def leastInterval(tasks: list[str], n: int) -> int:
    freq = dict()
    for task in tasks:
        freq[task] = freq.get(task, 0) + 1

    maxFreq = max(freq.values())
    maxCount = 0
    for _, value in freq.items():
        if value == maxFreq:
            maxCount += 1

    return max(len(tasks), (maxFreq - 1)*(n + 1)+maxCount)
