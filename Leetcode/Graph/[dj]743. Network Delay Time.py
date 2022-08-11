#dijskstra algo
# 743. Network Delay Time
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))
 
        heap = [(0,k)]
        visited = set()
        while heap:
            delay, node = heapq.heappop(heap)
            #to prevent cycles
            if node in visited:
                continue
            #addin to visited 
            visited.add(node)
            res = max(res, delay)
            for nxt, nxtdelay in adj[node]:
                if nxt not in visited:
                    heapq.heappush(heap,(delay + nxtdelay,nxt))
            
            
        return res if len(visited) == n else -1