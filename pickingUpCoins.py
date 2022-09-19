#The game question. A player can pick among the last 2 coins. What is the maximum sum?

def maximum_revenue(coins):
    def compute_maximum_revenue_for_range(a, b):
        if a > b:
            #No coins left
            return 0

        if maximum_revenue_for_range[a][b] == 0:
            max_revenue_a = coins[a] + min(compute_maximum_revenue_for_range(a + 2, b), compute_maximum_revenue_for_range(a + 1, b - 1))
            max_revenue_b = coins[b] + min(compute_maximum_revenue_for_range(a + 1, b - 1), compute_maximum_revenue_for_range(a, b - 2))
            maximum_revenue_for_range[a][b] = max(max_revenue_a, max_revenue_b)
        
        return maximum_revenue_for_range[a][b]

    maximum_revenue_for_range = [[0] * len(coins) for _ in coins]
    return compute_maximum_revenue_for_range(0, len(coins) - 1)

print(maximum_revenue([10,25,5,1,10,5]))
print(maximum_revenue([5,1,10,5]))
print(maximum_revenue([25,5,10,5,10,5,10,25,1,25,1,25,1,25,5,10]))