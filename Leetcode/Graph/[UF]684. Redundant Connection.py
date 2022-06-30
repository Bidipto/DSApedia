# 684. Redundant Connection

def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #union find by rank and path compression
    parent = [i for i in range(len(edges)+1)]
    rank = [1]*(len(edges)+1)
    #gives the parent of the node
    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node 
    
    def union(u,v):
        para = find(u)
        parb = find(v)
        if para == parb:
            return True 
        
        #ensurinf u's rank is always greater then v
        if rank[u]<rank[v]:
            u, v = v, u
            
        parent[parb] = para
        rank[u] += rank[v]
        
        return False 
    
    for u,v in edges:
        if union(u,v):
            return [u,v]