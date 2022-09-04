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

# Application of kruskals algorithm


import heapq
class Solution:
    #kruskal's algo with union find by rank and path compression 
    #significantlty faster then prims algo
    def par(self,node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self,u,v):
        paru = self.par(u)
        parv = self.par(v)
        
        #will form a cycle
        if paru == parv:
            return False
        
        if self.rank[parv]>self.rank[paru]:
            self.parent[paru] = parv
            self.rank[parv] += self.rank[paru]
        else:
            self.parent[parv] = paru
            self.rank[paru] += self.rank[parv]
        
        return True 
            
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        
        heap = []
        
        N = len(points)
        cost = 0
        
        for i,(x1,y1) in enumerate(points):
            for j,(x2,y2) in enumerate(points[i+1:],i+1):
                heapq.heappush(heap,(dis(x1,y1,x2,y2),i,j))
                # heapq.heappush(heap,(dis(x1,y1,x2,y2),j,i))
                
        # print(heap)
            
        self.parent = [i for i in range(N)]
        self.rank = [1] * N
             
        count = 0
        while count<N-1 and heap:
            w,u,v = heapq.heappop(heap)
            
            # print(w,u,v)
            # print(self.parent,self.rank,count)
            if self.union(u,v) == True:
                cost += w
                count += 1
                # print(count,cost)
                # print(self.parent,self.rank,count)
            # print()
            
        # print(self.parent,self.rank,count)
        return cost 
                    
def dis(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)