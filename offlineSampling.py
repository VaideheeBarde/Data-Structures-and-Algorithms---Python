import random
def random_sampling(k, A):
        for i in range(k):
                r = random.randint(i, len(A)-1)
                temp = A[i]
                A[i] = A[r]
                A[r] = temp

        return A

print(random_sampling(3,[5,11,3,7]))
print(random_sampling(4,[5,11,3,7]))