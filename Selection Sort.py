"""
    Selection Sort is a simple sorting algorithm that works by repeatedly selecting the minimum (or maximum) element from the unsorted part of the array and swapping it with the first element of the unsorted part.
    It sorts the array in-place, meaning it does not require additional memory to perform the sorting.
    O(n^2)
"""

def selection_sort(arr): 
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

<<<<<<< HEAD
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
=======
    return arr
>>>>>>> 299b5401fe33267c0aec11d9fd6a9ba11fc59a8f
