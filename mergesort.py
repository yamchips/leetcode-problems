def sort(arr1: list[int], arr2: list[int]) -> list[int]: 
    m, n = len(arr1), len(arr2)
    i, j = 0, 0
    res = []
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    if i < m:
        res.extend(arr1[i:])
    if j < n:
        res.extend(arr2[j:])
    return res

def mergesort(arr: list[int]) -> list[int]:
    n = len(arr)
    if n == 1 or n == 0:
        return arr
    left = mergesort(arr[:n//2])
    right = mergesort(arr[n//2:])
    return sort(left, right)
    
if __name__=='__main__':
    mergesort([1, 10, 7, 4, 6, 2, 5, 8, 9])