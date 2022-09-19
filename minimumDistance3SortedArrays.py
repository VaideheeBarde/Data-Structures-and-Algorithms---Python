#O(n log k) time complexity

import bintrees
import typing

def find_closest_elements_in_sorted_arrays(sorted_arrays):
    #Sorted array iterators in each entry
    iters = bintrees.RBTree()

    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it)

    min_distance_so_far = float('inf')
    while True:
        min_value, min_idx = iters.min_key()
        max_value = iters.max_key()[0]
        min_distance_so_far = min(max_value - min_value, min_distance_so_far)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        #Return if some array has no remaining elements
        if next_min is None:
            return typing.cast(int, min_distance_so_far)
        iters.insert((next_min, min_idx), it)

print(find_closest_elements_in_sorted_arrays([[1,2,3,4], [20,30,40,50], [3,4,5,6]]))