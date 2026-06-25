"""Question 1: Smallest integer greater than N with the same digit sum."""


def digit_sum(n: int) -> int:
    """Return the sum of digits of a non-negative integer."""
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


def solution(N: int) -> int:
    """
    Given an integer N, return the smallest integer greater than N
    whose digit sum is equal to the digit sum of N.
    """
    target = digit_sum(N)
    current = N + 1

    while True:
        if digit_sum(current) == target:
            return current
        current += 1


if __name__ == "__main__":
    test_cases = [
        (28, 37),
        (734, 743),
        (1990, 2089),
        (1000, 10000),
        (49999, 58999),
    ]

    for input_value, expected in test_cases:
        actual = solution(input_value)
        print(f"N = {input_value}, expected = {expected}, actual = {actual}")
        assert actual == expected

    print("All tests passed.")
