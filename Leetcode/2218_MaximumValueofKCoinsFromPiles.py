# 2218. Maximum Value of K Coins From Piles
#should not have taken more then 30 mins to do this
#already had this this idea before hand but didnt implemet it 
def maxValueOfCoins(self, piles: List[List[int]], K: int) -> int:
    dp = [[-1] * (K+1) for j in range(len(piles))]
    
    def magic(i,k):
        if k == K or i == len(piles):
            return 0
        
        if dp[i][k] != -1:
            return dp[i][k]
        
        curr = 0
        res = magic(i+1,k)
        
        for j in range(min(K-k,len(piles[i]))):
            curr += piles[i][j]
            res = max(res,curr + magic(i+1,k+j+1))
        
        dp[i][k] = res
        return dp[i][k]
    
    return magic(0,0)
                