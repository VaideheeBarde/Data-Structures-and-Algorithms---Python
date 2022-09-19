def change_making(cents):
    coins = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in coins:
        num_coins += cents//coin
        cents %= coin
    return num_coins

print(change_making(127))

#6 iterations
#Each iteration takes a constant amount of computation
#Time complexity is O(1)