def solution(input):
    def ispalindrome(i):
        # odd palindrome, centre is input[i]
        left, right = i, i
        while left >= 0 and right <= len(input) - 1:
            if input[left] == input[right]:
                left -= 1
                right += 1
            else:
                break
        # even palindrome, centre is input[i] and input[i + 1]
        left1, right1 = i , i + 1
        while left1 >= 0 and right1 <= len(input) - 1:
            if input[left1] == input[right1]:
                left1 -= 1
                right1 += 1
            else:
                break
        if right - left > right1 - left1 \
           or (right - left == right1 - left1 and \
               left < left1):
            return left + 1, right - 1
        elif right - left < right1 - left1 \
             or (right - left == right1 - left1 and \
                 left1 < left):
            return left1 + 1, right1 - 1
    
    palindrome_length = 0
    start, end = 0, 0
    for i in range(len(input)):
        left, right = ispalindrome(i)
        if right - left + 1 > palindrome_length or \
           (right - left + 1 == palindrome_length and left < start):
            start, end = left, right
            palindrome_length = right - left + 1
    return input[start: end + 1]

def solution(input):
    def ispalindrome(left, right):
        while left >= 0 and right <= len(input) - 1:
            if input[left] == input[right]:
                left -= 1
                right += 1
            else:
                break
        return left + 1, right - 1

    
    palindrome_length = 0
    start, end = 0, 0
    for i in range(len(input)):
        left_even, right_even = ispalindrome(i, i + 1)
        if right_even - left_even + 1 > palindrome_length:
            start, end = left_even, right_even
            palindrome_length = right_even - left_even + 1

        left_odd, right_odd = ispalindrome(i, i)
        if right_odd - left_odd + 1 > palindrome_length:
            start, end = left_odd, right_odd
            palindrome_length = right_odd - left_odd + 1
        
        
    return input[start: end + 1]

if __name__=="__main__":
    inputs = ["anna arrived at noon", "bob has a racecar", "bob has a racecar and a bike"]
    
    outputs = [solution(input) for input in inputs]
    print(outputs) # ["racecar", "a racecar a", "anna"]