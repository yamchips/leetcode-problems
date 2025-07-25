from collections import deque


def countDiff(gene1: str, gene2: str) -> int:
    count = 0
    for char1, char2 in zip(gene1, gene2):
        if char1 != char2:
            count += 1
    return count

def minMutation(startGene: str, endGene: str, bank: list[str]) -> int:
    if endGene not in bank:
        return -1
    
    queue = deque()
    queue.append(startGene)
    mutation = 0
    visited = set()
    while queue:
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()
            if curr == endGene:
                return mutation
            for gene in bank:
                if gene not in visited and countDiff(gene, curr) == 1:
                    queue.append(gene)
                    visited.add(gene)
        mutation += 1
    return -1