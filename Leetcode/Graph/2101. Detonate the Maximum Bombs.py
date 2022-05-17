# 2101. Detonate the Maximum Bombs
def maximumDetonation(self, bombs: List[List[int]]) -> int:
    #ADJ LIST 
    adj = defaultdict(list)
    N = len(bombs)
    for i in range(N):
        for j in range(N):
            if i == j: continue
            #using the distance formuale to check if the centre of j 
            #lies inside the circle if i
            radius = bombs[i][2]
            distance = (bombs[i][0]-bombs[j][0])**2+(bombs[i][1]-bombs[j][1])**2
            if radius**2 >= distance:
                adj[i].append(j)
    
    def dfs(node, visited):
        count = 1
        visited.add(node)
        for neighbour in adj[node]:
            if neighbour not in visited:
                count += dfs(neighbour,visited)
                
        return count
    
    res = 0
    for i in range(N):
        res = max(res, dfs(i,set()))
        
    return res