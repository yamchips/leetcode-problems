def minOperations(boxes: str) -> list[int]:
    n = len(boxes)
    # indices contains all '1' index
    indices = []
    for i in range(n):
        if boxes[i] == '1':
            indices.append(i)
    res = []
    ops = 0
    for i in range(n):
        for index in indices:
            ops += abs(index - i)
        res.append(ops)
        ops = 0
    return res