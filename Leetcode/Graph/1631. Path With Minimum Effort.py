# 1631. Path With Minimum Effort
# modified shortest path algorithn 
# dijsktra's algorithm
# since there is no negative weight cycle 
# we can use dijsktra's algorithm
# otherwise we had to use bellman ford algorithm or floyd warshall algorithm
def minimumEffortPath(self, arr: List[List[int]]) -> int:
        #2d map of efforts
        N = len(arr[0])
        M = len(arr)
        efforts = [[math.inf]*N for i in range(M)]
        efforts[0][0] = 0
        #bfs with a minheap (maxeffort,x,y)
        heap = [(0,0,0)]
        while heap:
            effort,x,y = heapq.heappop(heap)
            for m,n in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=m<M and 0<=n<N:
                    #next effort be max(maxeffort,absolute diff of current cell and next cell)
                    nexteffort = max(effort, abs(arr[x][y]-arr[m][n]))
                    #if next effort is less than the effort alreay stored in effort[nextx][nexty],
                    #we push nexteffort,nextx,nexty in the min heap
                    #for every iteration er will only be considering the path with the min effort
                    #cause it is stored in a minheap
                    if nexteffort < efforts[m][n]:
                        efforts[m][n] = nexteffort
                        heapq.heappush(heap,(nexteffort,m,n))
                    #iska sidha sidha matlab ye ha ki we found a new path with lower effort
                    #to reach [m][n], and hence we are recalculating the path with the new min effort
        return efforts[-1][-1]

#thora aur optimisation
def minimumEffortPath(self, arr: List[List[int]]) -> int:
        #2d map of efforts
        N = len(arr[0])
        M = len(arr)
        efforts = [[math.inf]*N for i in range(M)]
        efforts[0][0] = 0
        heap = [(0,0,0)]
        while heap:
            effort,x,y = heapq.heappop(heap)
            #since we are using a min heap we will always reach a point with lower effort first
            if x == M-1 and y == N-1:
                return effort
            for m,n in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if 0<=m<M and 0<=n<N:
                    nexteffort = max(effort, abs(arr[x][y]-arr[m][n]))
                    if nexteffort < efforts[m][n]:
                        efforts[m][n] = nexteffort
                        heapq.heappush(heap,(nexteffort,m,n))
        return efforts[-1][-1]