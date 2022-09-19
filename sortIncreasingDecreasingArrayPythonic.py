import heapq
import itertools

def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))

def sort_k_increasing_decreasing_array_pythonic(A):
    class Monotonic:
        def __init__(self):
            self._last = float('-inf')
        
        def __call__(self, curr):
            result = curr < self._last
            self._last = curr
            return result

    return merge_sorted_arrays_pythonic([list(group)[::-1 if is_decreasing else 1] for is_decreasing, group in itertools.groupby(A, Monotonic())])

print(sort_k_increasing_decreasing_array_pythonic([57,131,493,294,221,339,418,452,442,190]))