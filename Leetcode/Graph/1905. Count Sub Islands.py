class Solution:
    def countSubIslands(self, grid: List[List[int]], grid2: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        res = 0
        
        def magic(i,j):
            grid2[i][j] = 0
            temp = True
            for m,n in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=m<M and 0<=n<N and grid2[m][n]:
                    if not grid[m][n]: 
                        temp = False
                    if not magic(m,n):
                        temp = False
            return temp
       
        for m,n in product(range(M),range(N)):
            if grid[m][n] and grid2[m][n] and magic(m,n):
                res += 1
                
        return res