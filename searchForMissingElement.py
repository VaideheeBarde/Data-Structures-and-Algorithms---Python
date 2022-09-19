import collections
import functools

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))

def find_duplicate_missing(A):

    #Compute the xor of all the numbers from 0 to |A| - 1 and all entries in A
    miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)
    differ_bit, miss_or_dup = miss_xor_dup & (~(miss_xor_dup - 1)), 0
    print(differ_bit)

    for i, a in enumerate(A):
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    return (DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_xor_dup) if miss_or_dup in A else DuplicateAndMissing(miss_or_dup ^ miss_xor_dup, miss_or_dup))

print(find_duplicate_missing([3,1,0,3]))