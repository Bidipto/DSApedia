# 378. Kth Smallest Element in a Sorted Matrix

import heapq 
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        M = len(mat)
        N = len(mat[0])
        heap = []
        heapq.heappush(heap,(mat[0][0],0,0))
        s = set()
        while heap:
            val,x,y = heapq.heappop(heap)
            
            if (x,y) in s:
                continue
                
            s.add((x,y))
            
            if k == 1:
                return val
            
            # print(x,y,val,k)
            if x+1<M and (x+1,y) not in s:
                heapq.heappush(heap,(mat[x+1][y],x+1,y))
            
            if  y+1<N and (x,y+1) not in s:
                heapq.heappush(heap,(mat[x][y+1],x,y+1))
                
            k -= 1