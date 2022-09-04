#converted each box in 3*3 grid and then applied dfs to find the number of regions
#used 1s and 0s to make regions 

def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        
        mat = [[0]*(3*N) for i in range(N*3)]
        
        for i in range(N):
            for j in range(N):
                if grid[i][j] == "/":
                    m = i * 3
                    n = j * 3
                    mat[m+2][n] = 1
                    mat[m+1][n+1] = 1
                    mat[m][n+2] = 1
                elif grid[i][j] == "\\":
                    m = i * 3
                    n = j * 3
                    mat[m][n] = 1
                    mat[m+1][n+1] = 1
                    mat[m+2][n+2] = 1
        
        M = N*3
        def magic(m,n):
            mat[m][n] = 1
            
            for i,j in (m+1,n),(m-1,n),(m,n+1),(m,n-1):
                if 0<=i<M and 0<=j<M and mat[i][j] == 0:
                    magic(i,j)
                    
        res = 0
        
        for i in range(M):
            for j in range(M):
                # print(mat[i][j])
                if mat[i][j] == 0:
                    res += 1
                    magic(i,j)
                    # print(mat)
                    
        return res