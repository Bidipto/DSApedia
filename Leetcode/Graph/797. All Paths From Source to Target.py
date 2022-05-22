# 797. All Paths From Source to Target

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    #simple dfs from 0 kinda backtracking 
    #also no need of seen cause it acyclic and directed
    res = []
    
    def magic(i, curr):
        if i==len(graph)-1:
            res.append(curr)
            
        for nxt in graph[i]:
            magic(nxt,curr+[nxt])
            
    magic(0,[0])
    return res