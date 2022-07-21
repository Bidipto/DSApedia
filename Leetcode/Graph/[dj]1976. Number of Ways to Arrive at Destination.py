#modified dijkstra's algorithm
def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 1000000007
        adj = defaultdict(list)
        
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        #ways[i] will store the number of ways to i with distance[i] 
        #we will minimize distace with dijsktra's algo
        ways = [0]*n
        distance =[math.inf]*n
        heap = [(0,0)]
        
        #the number of ways to get to 0 will be 1 and its diatance will be 0
        ways[0] = 1
        distance[0] = 0
        
        while heap:
            d,u = heapq.heappop(heap)
            #if d is more the min distance discovered upto u then we dont process it
            if d>distance[u]:
                continue
                
            for v,w in adj[u]:
                if d+w<distance[v]:
                    distance[v] = d+w
                    ways[v] = ways[u]%mod
                    heapq.heappush(heap,(d+w,v))
                elif d+w == distance[v]:
                    ways[v] = (ways[u]+ways[v])%mod
                
                
        return ways[-1]%mod