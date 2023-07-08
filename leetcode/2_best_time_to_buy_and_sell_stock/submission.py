def maxProfit(prices):
    # Case where n-i > n, skip all checks
    # Only return best profit
    profit = 0
    start = prices[0]
    for price in prices:
        if price > start: # only care about the LOWEST stock price
            # e.g. [7,1,3,2,8] 1-8 has most profit
            # 2 does occur after but 1 is still smaller. 
            # We only need min value
            profit = max(price-start, profit)
        else:
            start = price

    return profit

print(maxProfit([7,1,6,4,3,5]))