def carPooling(trips: list[list[int]], capacity: int) -> bool:
    changes = [0] * 1001
    for number, start, end in trips:
        changes[start] += number
        changes[end] -= number
    total_passangers = 0
    for change in changes:
        total_passangers += change
        if total_passangers > capacity:
            return False

    return True
