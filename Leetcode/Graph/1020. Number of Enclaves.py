def numEnclaves(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        res = 0
        
        def magic(i,j):
            grid[i][j] = 0
            for m,n in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=m<M and 0<=n<N and grid[m][n] == 1:
                    magic(m,n)

        
        for n in range(N):
            if grid[0][n] == 1:
                magic(0,n)
            if grid[-1][n] == 1:
                magic(M-1,n)       
        for m in range(M):
            if grid[m][0] == 1:
                magic(m,0)
            if grid[m][-1] == 1:
                magic(m,N-1)
                
        
        return sum(sum(row) for row in grid)