def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=bool(i%2))

    return A

print(rearrange([3,2,4,1]))
print(rearrange([5,6,1,12,3]))