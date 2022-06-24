# 851. Loud and Rich

def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        #cached dfs, kinda dp on graph
        #first we make a adj list to go to richer people (reverse the order given)
        #cause for every person we are only concenred by the quietness of the richer people
        #and also note we dont have to return the min quietness of the richer people
        #we actually have to return the person who is quietest among richer then that person 
        N = len(quiet)
        adj = {i:[] for i in range(N)}
        res = [None]*N
        
        for u,v in richer:
            # print(v)
            adj[v].append(u)
        # print(adj)
        
        def magic(node):
            if res[node]:
                return res[node]
            
            res[node] = node
            for child in adj[node]:
                c = magic(child)
                if quiet[res[node]]>quiet[c]:
                    res[node] = c
                
            return res[node]
        
        for i in range(N):
            if not res[i]:
                res[i] = magic(i)
            # print(res,i)
        return res