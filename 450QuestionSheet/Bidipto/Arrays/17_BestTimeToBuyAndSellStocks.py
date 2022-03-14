def maxProfit(self, prices: List[int]) -> int:
    minn = prices[0]
    maxxProfit = 0
    #since we can go backwards and sell there for the max profit will be achieved with present or previous minn and 
    #selling at the maximum price in the future
    for price in prices:
        if price < minn:
            minn = price
        if price - minn > maxxProfit:
            maxxProfit = price - minn
    return maxxProfit