'''
List 
'''
def list_operation() -> None:
    nums = [3, 1, 4]

    nums.insert(1, 10)
    print(nums) # 3, 10, 1, 4

    # remove last element
    last_element = nums.pop()
    print(last_element) # 4

    # remove by index
    first_element = nums.pop(0)
    print(first_element) # 3

    # remove all elements
    nums.clear()

    nums = [3, 1, 4, 3]

    # remove first matching value
    nums.remove(3)
    print(nums) # 1, 4, 3

    # reverse copy
    reverse_nums = nums[::-1]
    print(reverse_nums)

    # reverse in-place
    nums.reverse()
    print(nums) # 3, 4, 1

    # count occurrence
    nums.append(3)
    occurrence = nums.count(3)
    print(occurrence) # 2

    # sort
    nums.sort()
    print(nums) # 1, 3, 3, 4

    # sort using lambda function
    nums.sort(key=lambda x: -x)
    print(nums) # 4, 3, 3, 1


