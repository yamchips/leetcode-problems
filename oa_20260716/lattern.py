'''
This simulates the process
Time complexity: O(coordinate range * len(objects))
'''
def lattern(objects, radius):
    
    max_count = 0
    best_center = float('inf')
    for center in range(objects[0] - radius, objects[-1] - radius + 1):
        lower = center - radius
        upper = center + radius
        count = 0
        for num in objects:
            if num < lower:
                continue
            else:
                if num <= upper:
                    count += 1
                else:
                    break
        if count > max_count:
            best_center = center
            max_count = count

    return best_center

'''
Sliding window solution. 

Here we move end index first inside the loop, that's feasible but it makes the code more complex. We can move the end index at the end. That leads us to the second Sliding window solution.
'''
def lattern(objects, radius):
    max_count = 0
    best_center = float('inf')

    start = 0
    end = 0
    n = len(objects)
    while end < n:
        
        while end < n and objects[end] - objects[start] <= 2 * radius:
           end += 1
        
        count = end - start
        if count > max_count:
            best_center = objects[end - 1] - radius
            max_count = count

        while end < n and objects[end] - objects[start] > 2 * radius:
            start += 1

    return best_center

'''
Another sliding window solution
'''
def lattern(objects, radius):
    max_count = 0
    best_center = 0
    left = 0
    
    for right in range(len(objects)):
    
        while objects[right] - objects[left] > 2 * radius:
            left += 1
    
        count = right - left + 1
    
        if count > max_count:
            max_count = count
            best_center = objects[right] - radius
    
    return best_center


if __name__=="__main__":
    print(lattern([-5,3,4,9], 5)) # -1
    print(lattern([-2,4,5,6,7], 1)) # 5