# 63. Unique Paths II
def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M=  len(grid)
        N = len(grid[0])
        dp = [[-1 for i in range(N)] for i in range(M)]
        
        if grid[-1][-1] != 0 or grid[0][0] != 0:
            return 0
        
        dp[-1][-1] = 1

        def magic(m, n):
            if dp[m][n] != -1:
                return dp[m][n]
            
            res = 0
            
            for i,j in (m+1,n),(m,n+1):
                if i<M and j<N and not grid[i][j]:
                    res += magic(i,j)
                        
            dp[m][n] = res    
            return dp[m][n]
        
        return magic(0,0)