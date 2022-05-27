# 934. Shortest Bridge
from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        que = deque()
        visited = set()
        #dfs for the first island to for the bfs que
        def dfs(i,j):
            que.append((i,j))
            for m,n in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=m<M and 0<=n<N and grid[m][n] == 1:
                    grid[m][n] = -1
                    dfs(m,n)
        

        for i,j in product(range(M), range(N)):
            if grid[i][j]:
                grid[i][j] = -1
                dfs(i,j)
                break
                
        
        #bfs on from the first island to the second island 
        level = -1
        while que:
            level += 1
            for i in range(len(que)):
                i,j = que.popleft()
                for m,n in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                    if 0<=m<M and 0<=n<N:
                        if grid[m][n] == 0:
                            grid[m][n] = -1
                            que.append((m,n))
                        elif grid[m][n]==1:
                            return level