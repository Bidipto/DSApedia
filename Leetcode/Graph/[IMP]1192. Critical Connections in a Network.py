# 1192. Critical Connections in a Network
# remove bridges by rank 
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        
        adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
            
        res = []
            
        rank = [-1 for i in range(n)]
        visited = set()
        
        def dfs(i,currrank, prev):
            rank[i] = currrank
            visited.add(i)
            
            for nxt in adj[i]:
                if nxt == prev:
                    continue
                    
                if nxt not in visited:
                    dfs(nxt,currrank+1,i)
                    
                rank[i] = min(rank[i],rank[nxt])
                
                if currrank<rank[nxt]:
                    res.append([i,nxt])
                    
        dfs(0,0,-1)
        
        return res