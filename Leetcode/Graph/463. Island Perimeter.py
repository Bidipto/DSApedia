# 463. Island Perimeter
def islandPerimeter(self, grid: List[List[int]]) -> int:
        #this solution can be done with just two loops istead of a dfs solution
        M = len(grid)
        N = len(grid[0])
        # debug = [([-1]*N) for i in range(M)]
        def magic(i,j):
            currPerimeter  = 4
            perimeter = 0
            for m,n in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=m<M and 0<=n<N:
                    if grid[m][n] == 1:
                    #when we have unvisted cell we visit that and 
                    #perimerter by 1
                        grid[m][n] = -1
                        currPerimeter -= 1
                        perimeter += magic(m,n)
                    #if we have a visited cells by side we decrease peri by 1
                    elif grid[m][n] == -1:
                        currPerimeter -= 1
            # debug[i][j] = perimeter + currPerimeter
            return perimeter + currPerimeter

        for i,j in product(range(M), range(N)):
            if grid[i][j] == 1:
                grid[i][j] = -1
                return magic(i,j)
