from collections import defaultdict
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        #classic bfs
        #adj key->stop, values->bus routes hence reffered bus number  
        adj = defaultdict(list)
        for busno,stops in enumerate(routes):
            for stop in stops:
                 adj[stop].append(busno)
        # print(adj) 
        
        queue = deque([source])
        visited = set([source])
        counter = 0
        
        while queue:
            counter += 1
            for q in range(len(queue)):
                start = queue.popleft()
                #looping throught the buses through the start stop
                for busno in adj[start]:
                    for end in routes[busno]:
                        if end in visited:
                            continue
                        elif end == target:
                            return counter
                        else:
                            queue.append(end)
                            visited.add(end)
                    routes[busno] = []
                    
        return -1