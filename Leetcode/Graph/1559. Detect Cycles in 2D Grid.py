# 1559. Detect Cycles in 2D Grid
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        M = len(grid)
        N = len(grid[0])
        
        def magic(i,j,prev):
            if (i,j) in visited:
                return True

            visited.add((i,j))
            
            for m,n in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=m<M and 0<=n<N and grid[i][j] == grid[m][n] and (m,n) != prev:
                    if magic(m,n,(i,j)):
                        return True
            
            return False
                    
        for m in range(M):
            for n in range(N):
                if (m,n) not in visited and magic(m,n,(-1,-1)):
                        return True
                
        return False