import collections

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_subarray_covering_set(paragraph, keywords):
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(-1, -1)
    remaining_to_cover = len(keywords)
    left = 0

    for right, p in enumerate(paragraph):
        if p in keywords_to_cover:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        #Keep advancing left until keywords_to_cover does not contain all keywords
        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = Subarray(left, right)
            p1 = paragraph[left]
            if p1 in keywords:
                keywords_to_cover[p1] += 1
                if keywords_to_cover[p1] > 0:
                    remaining_to_cover += 1
            left += 1

    return result

paragraph = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple', 'cat', 'dog', 'banana']
keywords = ('banana', 'cat')

print(find_smallest_subarray_covering_set(paragraph, keywords))