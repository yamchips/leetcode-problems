from collections import defaultdict

def totalFruit(fruits: list[int]) -> int:
    max_fruit = 0
    record = defaultdict(int)
    start = 0
    for end in range(len(fruits)):
        while len(record) == 2 and fruits[end] not in record:
            record[fruits[start]] -= 1
            if record[fruits[start]] == 0:
                del record[fruits[start]]
            start += 1

        record[fruits[end]] += 1
        max_fruit = max(max_fruit, end - start + 1)

    return max_fruit
