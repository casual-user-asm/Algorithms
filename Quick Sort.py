"""
    Quicksort is a highly efficient, comparison-based sorting algorithm that follows the divide-and-conquer strategy to sort an array or list of elements.
    O(n log n)
"""

def quickSort(data):

    if len(data) <= 1:
        return data
    
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]

    return quickSort(left) + middle + quickSort(right)
