def bsearch(t, A):
    L, U = 0, len(A) - 1
    while L <= U:
        #M = (L + U) // 2
        M = L + (U - L)/2
        
        if A[M] < t:
            L = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1

    return -1

print(bsearch(5, [1,2,3,4,5]))