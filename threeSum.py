def has_two_sum(A, t):
    i, j = 0, len(A) - 1

    while i<=j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j]  < t:
            i += 1
        else:
            j -= 1

    return False

def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t - a) for a in A)

print(has_three_sum([-2,1,2,4,7,11], 40))
print(has_three_sum([-2,1,2,4,7,11], 10))