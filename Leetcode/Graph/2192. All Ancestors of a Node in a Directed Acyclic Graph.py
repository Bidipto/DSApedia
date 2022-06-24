# 2192. All Ancestors of a Node in a Directed Acyclic Graph

def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        N = n
        
        adj = [[] for i in range(N)]
        
        #reversed and also the relations is 1 indexed 
        for v,u in edges:
            adj[u].append(v)
            
        res = [set() for i in range(N)]
        visited = set()
        
        def magic(node):
            visited.add(node)
            
            for child in adj[node]:
                if child not in visited:
                    magic(child)
                res[node].update(res[child])
                res[node].add(child)
            
            
            
        
        for i in range(N):
            if i not in visited:
                magic(i)
                
        for node in range(N):
            res[node] = sorted(list(res[node]))
                
        return res