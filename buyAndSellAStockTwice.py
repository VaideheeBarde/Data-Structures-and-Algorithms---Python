def buy_and_sell_stock_twice(prices):
    max_total_profit = 0.0
    min_price_so_far = float('inf')
    first_buy_sell_profits = [0.0]*len(prices)

    #Forward phase
    #For each day, we record maximum profit is we sell on that day

    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price-min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    #Backward phase
    #For each day, find the maximum profit if we make the second buy on that day

    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far-price+first_buy_sell_profits[i-1])
    return max_total_profit

print(buy_and_sell_stock_twice([310, 310, 275, 275, 260, 260, 260, 230, 230, 230, 350]))