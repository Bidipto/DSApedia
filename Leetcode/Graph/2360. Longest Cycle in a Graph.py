# 2360. Longest Cycle in a Graph
# kinda came up with this one myself
def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        
        seen = set()
        
        count = dict()
        
        self.res = -1
        
        def magic(node,curr):
            if node not in seen:
                if node in count:
                    self.res = max(self.res,curr-count[node])
                    return 
                if edges[node] != -1:
                    count[node] = curr
                    magic(edges[node],curr+1)
                    del count[node]
                seen.add(node)

        for i in range(N):
            magic(i,0)
            
        return self.res