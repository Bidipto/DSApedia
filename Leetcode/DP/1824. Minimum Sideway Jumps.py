# 1824. Minimum Sideway Jumps
def minSideJumps(self, obstacles: List[int]) -> int:
        #each dp state says the number of jumps to get to that lane at that obstacle
        dp = [1,0,1]
        
        for i in obstacles:
            if i:
                dp[i-1] = math.inf
            for lane in range(3):
                if lane != i-1:
                    dp[lane] = min(dp[lane],dp[(lane+1)%3]+1,dp[(lane+2)%3]+1) 
        return min(dp)