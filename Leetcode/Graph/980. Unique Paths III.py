# 980. Unique Paths III

#simple dfs with a addition counter to count the number of steps
def magic(self, m, n, count, grid):
    #out of bounds and obstacles
    if m<0 or m>=self.M or n<0 or n>=self.N or grid[m][n]<0 or count<0:
        return
    
    if grid[m][n] == 2:
        if count == 0:
            self.res += 1
        return 
    
    grid[m][n] = -2
    
    self.magic(m+1, n, count-1, grid)
    self.magic(m-1, n, count-1, grid)
    self.magic(m, n+1, count-1, grid)
    self.magic(m, n-1, count-1, grid)
    
    grid[m][n] = 0
    
def uniquePathsIII(self, grid: List[List[int]]) -> int:
    count = 1
    # self.grid = grid
    self.M = len(grid)
    self.N = len(grid[0])
    self.res = 0