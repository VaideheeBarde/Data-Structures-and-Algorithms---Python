import heapq

def kth_largest_in_heap(A, k):
    if k <= 0:
        return []

    candidate_max_heap = []
    candidate_max_heap.append((-A[0], 0))
    result = []

    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))

        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))

    return result

print(kth_largest_in_heap([561, 314, 401, 28, 156, 359, 271, 11, 3], 3))