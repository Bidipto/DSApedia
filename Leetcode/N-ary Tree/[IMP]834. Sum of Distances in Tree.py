# 834. Sum of Distances in Tree

def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        #in the first dfs we will be searchign for the distance of children in a node, ie the depth 
        #and also the weight ie the number of nodes connected 
        
        weights = [0]*N
        depths = [0]*N
        res = [0]*N
        
        def magic(node,depth,par):
            weights[node] = 1
            depths[node] = depth
            for child in adj[node]:
                if child != par:
                    weights[node] += magic(child,depth+1,node)
            return weights[node]
        
        magic(0,0,-1)
        
        def moremagic(node,r,par):
            for child in adj[node]:
                if child != par:
                    res[child] = r + (N - weights[child]) - weights[child]
                    moremagic(child,res[child],node)
        
        res[0] = sum(depths)
        moremagic(0,res[0],-1)
        
        # print(weights , depths)
        
        return res
    