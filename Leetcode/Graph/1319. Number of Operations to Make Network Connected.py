# 1319. Number of Operations to Make Network Connected
def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #if the number of connections is less than n-1 then 
        #under no circumstances its possible we connect all the nodes
        #and if its equal or more the n-1 then we can connect all the the nodes
        #we just need to return the number of components - 1
        if len(connections)<n-1:
            return -1
        
        adj = defaultdict(list)
        res = -1
        
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        seen = [False] * n
        
        def magic(i):
            if seen[i]:
                return 

            seen[i] = True
            for neighbour in adj[i]:
                if not seen[neighbour]:
                    magic(neighbour)
                    
        for i in range(n):
            if not seen[i]:
                res += 1
                magic(i)
                
        return res