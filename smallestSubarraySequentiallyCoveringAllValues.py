import collections

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_sequentially_covering_subset(paragraph, keywords):
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    shortest_subarray_length = [float('inf')] * len(keywords)
    shortest_distance = float('inf')
    result = Subarray(-1, -1)

    for i, p in enumerate(paragraph):

        if p in keyword_to_idx:

            keyword_idx = keyword_to_idx[p]

            if keyword_idx == 0:
                shortest_subarray_length[keyword_idx] = 1

            elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
                distance_to_previous_keyword = (i - latest_occurrence[keyword_idx - 1])
                shortest_subarray_length[keyword_idx] = (distance_to_previous_keyword + shortest_subarray_length[keyword_idx - 1])

            latest_occurrence[keyword_idx] = i

            #Last keyword, for improved subarray
            if (keyword_idx == len(keywords) - 1 and shortest_subarray_length[-1] < shortest_distance):
                shortest_distance = shortest_subarray_length[-1]
                result = Subarray(i - shortest_distance + 1, i)

    return result

paragraph = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple', 'cat', 'dog', 'banana']
keywords = ('banana', 'cat')

print(find_smallest_sequentially_covering_subset(paragraph, keywords))