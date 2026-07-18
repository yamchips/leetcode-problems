'''
Given an array of integers. Check its even index elements. If they are in decreasing order, return 'Decreasing'; If they are in increasing order, return 'Increasing'; Otherwise, return 'None'.
'''

def even_array(arr: list):
    even_elements = arr[::2]
    if all(a > b for a, b in zip(even_elements, even_elements[1:])):
        return "Decreasing"
    if all(a < b for a, b in zip(even_elements, even_elements[1:])):
        return "Increasing"
    return "None"



if __name__=="__main__":
    print(even_array([1, 23, 4, 3, 6, -3])) # Increasing
    print(even_array([1, 23, 4, 3, -6, -3])) # None
    print(even_array([10, 0, 8, 23, 4, -2])) # Decreasing