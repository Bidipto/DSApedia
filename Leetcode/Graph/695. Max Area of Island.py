# 695. Max Area of Island
# similar to number of islands but here we  just return the number of cells in an island 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        res = 0
        def magic(i,j):
            temp = 1
            for m,n in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=m<M and 0<=n<N and grid[m][n] == 1:
                    grid[m][n] = -1
                    temp += magic(m,n)        
            return temp
        

        for i,j in product(range(M), range(N)):
            if grid[i][j] == 1:
                grid[i][j] = -1
                res = max(res,magic(i,j))
                 
        return res