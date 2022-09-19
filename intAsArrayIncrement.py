#input = 99999, output = 99999 + 1= 100000
#input = 91012139, output = 91012140

def plus_one(A):
    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i]!=10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        #there is a carry-out so we need one more digit to store the result
        #a slick way to do this is to append the result at the end of the array
        #and update the first entry to 1
        A[0] = 1
        A.append(0)

    return A

print(plus_one([9,9,9,9,9]))
print(plus_one([9,10,12,13,9]))