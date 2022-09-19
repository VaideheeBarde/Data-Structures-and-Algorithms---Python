def merge_two_sorted_arrays(A, m, B, n):
    a, b, write_idx = m - 1, n - 1, m + n - 1
    C = [None] * (m + n)

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            C[write_idx] = A[a]
            a -= 1
        else:
            C[write_idx] = B[b]
            b -= 1
        write_idx -= 1

    while a >= 0:
        C[write_idx] = A[a]
        write_idx -= 1
        a -= 1

    while b >= 0:
        C[write_idx] = B[b]
        write_idx -= 1
        b -= 1

    return C

A = [1,3,5,7]
m = len(A)
B = [2,4,6,8]
n = len(B)
print(merge_two_sorted_arrays(A, m, B, n))

A = [3,13,17]
m = len(A)
B = [3,7,11,19]
n = len(B)
print(merge_two_sorted_arrays(A, m, B, n))