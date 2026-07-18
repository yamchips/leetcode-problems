'''
Currently, it's incorrect.
'''
def solution(board, pattern):
    rows = len(board)
    cols = len(board[0])
    size = len(pattern)

    for start_row in range(rows - size + 1):
        for start_col in range(cols - size + 1):
            letter_to_digit = {}
            used_digits = set()
            matches = True

            for r in range(size):
                for c in range(size):
                    pattern_value = pattern[r][c]
                    board_value = board[start_row + r][start_col + c]

                    if pattern_value.isdigit():
                        if int(pattern_value) != board_value:
                            matches = False
                            break

                    else:
                        if pattern_value in letter_to_digit:
                            if letter_to_digit[pattern_value] != board_value:
                                matches = False
                                break
                        else:
                            if board_value in used_digits:
                                matches = False
                                break

                            letter_to_digit[pattern_value] = board_value
                            used_digits.add(board_value)

                # Outside the c loop, inside the r loop
                if not matches:
                    break

            # Outside both r and c loops
            if matches:
                return [start_row, start_col]

    return [-1, -1]