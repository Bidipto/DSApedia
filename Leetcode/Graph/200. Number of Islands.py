# 200. Number of Islands
# simple dfs on all islands and count the number of islands
# instead of using a visited set, use a grid to mark the visited as -1 
def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        res = 0
        def dfs(i,j):
            for m,n in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=m<M and 0<=n<N and grid[m][n] == '1':
                    grid[m][n] = -1
                    dfs(m,n)
        

        for i,j in product(range(M), range(N)):
            if grid[i][j] == '1':
                res += 1
                grid[i][j] = -1
                dfs(i,j)
                
        return res