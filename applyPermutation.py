def apply_permutation(perm, A):
    for i in range(len(A)):
        while perm[i] != i:
            temp = A[i]
            A[i] = A[perm[i]]
            A[perm[i]] = temp

            temp = perm[perm[i]]
            perm[perm[i]] = perm[i]
            perm[i] = temp

    return A

print(apply_permutation([3,2,1,0], ['a','b','c','d']))
print(apply_permutation([1,0,3,2], ['a','b','c','d']))