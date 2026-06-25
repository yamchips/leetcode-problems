"""Question 2: Word machine stack operations."""

MAX_VALUE = 2**20 - 1


def is_valid_int(s: str) -> bool:
    """Return True if s is a non-negative integer token."""
    return s.isdigit()


def solution(S: str) -> int:
    """
    Process a sequence of word-machine operations.

    Supported operations:
    - integer X: push X
    - DUP: duplicate topmost value
    - POP: remove topmost value
    - +: add top two values
    - -: subtract second topmost value from topmost value

    Return -1 if an error occurs.
    """
    stack = []

    for command in S.split():
        if is_valid_int(command):
            value = int(command)
            if value > MAX_VALUE:
                return -1
            stack.append(value)

        elif command == "DUP":
            if not stack:
                return -1
            stack.append(stack[-1])

        elif command == "POP":
            if not stack:
                return -1
            stack.pop()

        elif command == "+" or command == "-":
            if len(stack) < 2:
                return -1
            first = stack.pop()
            second = stack.pop()
            if command == "+" :
                result = first + second
            else:
                result = first - second
            if result > MAX_VALUE or result < 0:
                return -1
            stack.append(result)
            
    return -1 if not stack else stack[-1]


if __name__ == "__main__":
    test_cases = [
        ("4 5 6 - 7 +", 8),
        ("13 DUP 4 POP 5 DUP + DUP + -", 7),
        ("5 6 + -", -1),
        ("3 DUP 5 - -", -1),
        ("1048575 DUP +", -1),
        ("DUP", -1),
        ("POP", -1),
        ("", -1),
    ]

    for input_value, expected in test_cases:
        actual = solution(input_value)
        print(f"S = {input_value!r}, expected = {expected}, actual = {actual}")
        assert actual == expected

    print("All tests passed.")
