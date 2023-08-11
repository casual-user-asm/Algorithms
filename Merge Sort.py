"""
    Merge sort is a popular sorting algorithm that follows the divide-and-conquer paradigm to efficiently sort an array or list of elements. 
    O(n)
"""

def merger(data):
    if len(data) > 1:

        mid = len(data) // 2
        r = data[:mid]
        l = data[mid:]

        merger(r)
        merger(l)

        i = j = k = 0

        while i < len(r) and j < len(l):
            if r[i] < l[j]:
                data[k] = r[i]
                i += 1
            else:
                data[k] = l[j]
                j += 1
            k += 1

        while i < len(r):
            data[k] = r[i]
            i += 1
            k += 1

        while j < len(l):
            data[k] = l[j]
            j += 1
            k += 1
    
    return data
