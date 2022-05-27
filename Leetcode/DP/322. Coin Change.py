# 322. Coin Change
def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        
        #for each amount we check all the coins we can use and then minimize the amount
        for i in range(amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
                    
        return dp[-1] if dp[-1]!=math.inf else -1