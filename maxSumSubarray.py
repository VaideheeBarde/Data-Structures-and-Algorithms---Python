def find_maximum_subarray(A):
    max_seen = float('-inf')
    max_end = 0

    for a in A:
        max_end = max(a, a + max_end)
        max_seen = max(max_seen, max_end)

    return max_seen

A = [-2]
print(find_maximum_subarray(A))
B = [904, 40, 523, 12, -335, -385, -124]
print(find_maximum_subarray(B))