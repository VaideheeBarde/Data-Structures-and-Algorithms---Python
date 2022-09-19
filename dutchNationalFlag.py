def dutchNationalFlag(pivot_index, A):
    pivot = A[pivot_index]

    #first pass: group smaller than pivot
    for i in range(len(A)):

        #look for a smaller element
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                break

    #second pass: group elements larger than pivot
    for i in reversed(range(len(A))):

        #look for larger element
        #stop when we reach an element less than pivot
        #since first pass has moved them to the start of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                break

    return A

print(dutchNationalFlag(3, [3,3,8,7,8]))
print(dutchNationalFlag(2, [4,2,1,3]))