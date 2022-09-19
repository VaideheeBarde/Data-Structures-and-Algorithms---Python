import heapq

def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []

    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result

def sort_k_increasing_decreasing_array(A):
    sorted_subarrays = []
    increasing, decreasing = range(2)
    subarray_type = increasing
    start_idx = 0

    for i in range(1, len(A) + 1):
        if (i==len(A) or (A[i-1]<A[i] and subarray_type == decreasing) or (A[i-1] > A[i] and subarray_type == increasing)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type == increasing else A[i-1:start_idx-1:-1])
            start_idx = i
            subarray_type = (decreasing if subarray_type == increasing else increasing)

    return merge_sorted_arrays(sorted_subarrays)

print(sort_k_increasing_decreasing_array([57,131,493,294,221,339,418,452,442,190]))