def characterReplacement(s: str, k: int) -> int:
    maxLength = 0
    # freq record the occurrence of 26 characters
    freq = [0] * 26
    left = 0
    for right in range(len(s)):
        freq[ord(s[right]) - ord('A')] += 1

        # current window size - max value in freq <= k, window is valid
        while right - left + 1 - max(freq) > k:
            # window is invalid, update window and move left pointer
            freq[ord(s[left]) - ord('A')] -= 1
            left += 1
        
        # window is valid
        maxLength = max(maxLength, right - left + 1)

    return maxLength
