# 466. Reorder Routes to Make All Paths Lead to the City Zero
from collections import defaultdict,deque
#just used opposite connection and counted them
#as there is only one way to reach a node
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        reverse = defaultdict(list)
        
        for u,v in connections:
            adj[u].append(v)
            reverse[v].append(u)
                  
        que = deque([0])
        counter = 0
        visited = set([0])
        
        while que:
            for k in range(len(que)):
                start = que.popleft()
                for end in adj[start]:
                    if end not in visited:
                        counter += 1
                        que.append(end)
                        visited.add(end)
                for end in reverse[start]:
                    if end not in visited:
                        que.append(end)
                        visited.add(end)
                        
        return counter 
        