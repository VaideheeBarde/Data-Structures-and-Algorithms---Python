#Compute size k subsets of {1,2,...,n}
#k = 2, n = 5
#[[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]

def combinations(n, k):
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(partial_combination.copy())
            return

        num_remaining = k - len(partial_combination)
        i = offset

        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i + 1, partial_combination + [i])
            i += 1

    result = []
    directed_combinations(1, [])
    return result

print(combinations(5, 2))