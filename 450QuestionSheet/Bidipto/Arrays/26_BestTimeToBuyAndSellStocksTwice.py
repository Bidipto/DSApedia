#The dp approach which could be generalized to k times
def maxProfit(self, prices: List[int]) -> int:
    K = 2
    dp = [[[-1 for i in range(2)] for _ in range(K)] for j in range(len(prices) - 1)]
    def magic(num, buy, k, dp):
        if k == K:
            return 0
        if num == len(prices) - 1:
            if buy:
                return 0
            if not buy:
                return prices[-1]

        if dp[num][buy][k] != -1:
            return dp[num][buy][k]

        if buy:
            take = magic(num + 1, not buy, k, dp) - prices[num]
            # print(num, take, buy)    
        else:
            take = magic(num + 1, not buy, k + 1, dp) + prices[num]
            # print(num, take, buy)

        nottake = magic(num + 1, buy, k, dp)
        # print(num, take, nottake)

        dp[num][buy][k] = max(take, nottake)
        # print(num, buy, dp, take, nottake, k)

        return dp[num][buy][k]

    return magic(0, True, 0, dp)
#Not so dp approach 
def maxProfit(self, prices: List[int]) -> int:
    profit1 = 0
    profit2 = 0
    moneyini = math.inf
    moneyafter1 = -math.inf
    for i in prices:
        #minimizing the initial money
        moneyini = min(moneyini, i)
        #maximizing the money after selling the first stock stock
        profit1 = max(profit1, i - moneyini)
        #maximizing the money after buying the second stock
        moneyafter1 = max(moneyafter1, profit1 - i)
        #maximizing the money after selling the second stock
        profit2 = max(profit2, moneyafter1 + i)
    return profit2