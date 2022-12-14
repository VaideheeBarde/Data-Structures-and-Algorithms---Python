def longest_nondecreasing_subsequence_length(A):
    #max_length[i] holds the length of the longest non decreasing sequence of A[:i+1]
    max_length = [1] * len(A)

    for i in range(1, len(A)):
        max_length[i] = 1 + max((max_length[j] for j in range(i) if A[i] >= A[j]), default=0)

    return max(max_length)

print(longest_nondecreasing_subsequence_length([0,8,4,12,2,10,6,14,1,9]))