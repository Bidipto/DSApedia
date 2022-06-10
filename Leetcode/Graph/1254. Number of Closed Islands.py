def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        M = len(grid)
        N = len(grid[0])
        #we will only call if we have a 1 already
        def magic(i,j):
            grid[i][j] = 1
            temp = True
            for m,n in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=m<M and 0<=n<N and grid[m][n] == 0:
                    if m == 0 or m == M-1 or n == 0 or n == N-1:
                        temp = False  
                    if not magic(m,n):
                        temp = False
            return temp
                                
        for i,j in product(range(M),range(N)):
            if grid[i][j] == 0 and magic(i,j) and not (i == 0 or i == M-1 or j == 0 or j == N-1):
                res += 1
        return res