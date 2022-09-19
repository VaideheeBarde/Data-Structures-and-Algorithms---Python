#reorder an array 
#such that the even entries appear first

def evenOdd(A):
    nextEven = 0
    nextOdd = len(A)-1

    while nextEven < nextOdd:
        if A[nextEven]%2==0:
            nextEven += 1

        else:
            temp = A[nextEven]
            A[nextEven] = A[nextOdd]
            A[nextOdd] = temp
            nextOdd -= 1

    return A

print(evenOdd([1,2,11,13,8]))
print(evenOdd([1,2,3,4,5,6]))