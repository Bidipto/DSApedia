# 1034. Coloring A Border
from collections import deque
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        default = grid[row][col]
        M = len(grid)
        N = len(grid[0])
        que = deque([(row,col)])
        seen = set()
        
        while que:
            # print(grid[0])
            # print(grid[1])
            # print(grid[2])
            # print()
            for q in range(len(que)):
                i,j = que.popleft()
                
                if (i,j) in seen:
                    continue
                seen.add((i,j))
                
                for m,n in (i,j+1),(i,j-1),(i+1,j),(i-1,j):
                    if 0<=m<M and 0<=n<N and grid[m][n] == default:
                        if (m,n) not in seen:
                            que.append((m,n))
                    elif (m,n) not in seen:
                        grid[i][j] = color
        return grid