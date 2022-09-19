import heapq
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))

print(merge_sorted_arrays_pythonic([[3,5,7],[0,6],[0,6,28]]))