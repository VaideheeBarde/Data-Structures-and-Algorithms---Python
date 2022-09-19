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

print(has_two_sum([-2,1,2,4,7,11], 10))
print(has_two_sum([-2,1,2,4,7,11], 6))
print(has_two_sum([-2,1,2,4,7,11], 13))