#classic bfs
def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #if start or end is unreachable 
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        M = len(grid)
        N = len(grid[0])
        
        level = 0
        que = deque([(0,0)])
        while que:
            level -= 1
            # print(que,-level)
            for q in range(len(que)):
                i,j = que.popleft()
                #end is reached
                if i == N-1 and j == M-1:
                    return -level
                #if already visited 
                if grid[i][j] != 0:
                    continue
                    
                grid[i][j] = level
                
                for m,n in (i+1,j+1),(i+1,j),(i+1,j-1),(i,j+1),(i,j-1),(i-1,j+1),(i-1,j),(i-1,j-1):
                    if 0<=m<M and 0<=n<N and grid[m][n] == 0:
                        que.append((m,n))
        return -1