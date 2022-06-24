# 2050. Parallel Courses III

def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
    N = len(time)
    
    adj = [[] for i in range(N)]
    
    #reversed and also the relations is 1 indexed 
    for v,u in relations:
        adj[u-1].append(v-1)
        
    res = [None]*N
    
    def magic(node):
        if res[node]:
            return res[node]
        
        res[node] = 0
        for child in adj[node]:
            res[node] = max(res[node],magic(child))
            
        res[node] += time[node]
        return res[node]
    
    for i in range(N):
        if not res[i]:
            res[i] = magic(i)
            
    return max(res)