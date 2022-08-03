# 778. Swim in Rising Water

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #instead of the edge weight we keep track of the max height seen 
        #dijsktra algo modification 
        N = len(grid)
        
        if N == 1:
            return grid[0][0]
        
        heap = [(grid[0][0],0,0)]
        seen = set()
        
        while heap:
            val,x,y = heapq.heappop(heap)
             
            
            for m,n in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if (m,n) in seen or m<0 or m>N-1 or n<0 or n>N-1: continue
                    
                if m == N-1 and n ==N-1:
                    return max(val,grid[m][n])
                
                seen.add((m,n))
                
                heapq.heappush(heap, (max(val,grid[m][n]),m,n))