"""
    Selection Sort is a simple sorting algorithm that works by repeatedly selecting the minimum (or maximum) element from the unsorted part of the array and swapping it with the first element of the unsorted part.
    It sorts the array in-place, meaning it does not require additional memory to perform the sorting.
"""

def selection_sort(arr):
    
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]