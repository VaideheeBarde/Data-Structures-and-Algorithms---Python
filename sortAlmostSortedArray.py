import itertools
import heapq

def sort_approximately_sorted_array(sequence, k):
    min_heap = []

    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    result = []

    for x in range(k, len(sequence)):
        smallest = heapq.heappushpop(min_heap, sequence[x])
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result

print(sort_approximately_sorted_array([3,-1,2,6,4,5,8], 2))