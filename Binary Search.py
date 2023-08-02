"""
    Binary search is an efficient searching algorithm used to find the position of a target value within a sorted array.
    The algorithm works by repeatedly dividing the search space in half until the target value is found or until the search space is empty, indicating that the target is not present in the array.
"""

def binary_search(data, element):
    
    min_index = 0
    max_index = len(data) - 1

    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2

        if data[mid_index] == element:
            return mid_index
        elif data[mid_index] < element:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    
    return 'No element in sequence'