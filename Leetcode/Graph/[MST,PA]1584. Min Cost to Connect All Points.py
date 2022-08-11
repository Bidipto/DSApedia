# Application of prims algorithm
def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        adj = {i:[] for i in range(N)}
        
        #adj list 
        #pre processing the node with the weights of the edges
        for i in range(N):
            xi,yi = points[i]
            for j in range(i+1,N):
                xj,yj = points[j]
                cost = abs(xi-xj) + abs(yi-yj)
                adj[i].append([cost,j])
                adj[j].append([cost,i])
                
        #vanilla prims algo 
        visited = set()
        heap = [[0,0]]
        res = 0
        
        while len(visited)<N:
            cost,node = heapq.heappop(heap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for nxtcost,nxt in adj[node]:
                if nxt not in visited:
                    heapq.heappush(heap,[nxtcost, nxt])
                
        return res