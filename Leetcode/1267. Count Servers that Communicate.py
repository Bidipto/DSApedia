# 1267. Count Servers that Communicate
def countServers(self, grid: List[List[int]]) -> int:
    rows = Counter()
    cols = Counter()
    M = len(grid)
    N = len(grid[1])
    for i,j in product(range(M),range(N)): 
        if grid[i][j]:
            rows[i]+=1
            cols[j]+=1
    res = 0       
    for i,j in product(range(M),range(N)):
        #atleast the row or the column has more then two servers
        if grid[i][j] and rows[i] + cols[j]>2:
            res += 1
            
    return res