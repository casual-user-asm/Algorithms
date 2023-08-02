"""
    Insertion Sort is a simple sorting algorithm that works by building a sorted list one element at a time.
    It is an "in-place" sorting algorithm, meaning it does not require any additional data structures to perform the sorting; the sorting is done directly on the original array.
"""

def insertion_sort(arr):
    
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        q = i - 1

        while q >= 0 and arr[q] > key:
            arr[q+1] = arr[q]
            q -= 1

        arr[q+1] = key

    return arr
