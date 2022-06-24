# 787. Cheapest Flights Within K Stops
#Bellman Ford shortest path algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        arr = [math.inf] * n
        arr[src] = 0
        for k in range(k+1):
            temp = arr.copy()
            for u,v,w in flights:
                if temp[u] != math.inf:
                    #comparing values cause we need te use a flight path with
                    #currstops - 1 stops 
                    #else if we use a path cost in temp 
                    #we would be using a path with currstops while calculating 
                    #a path with curr stops 
                    if arr[u] + w < temp[v]:
                        temp[v] = arr[u] + w
            arr = temp
        
        return arr[dst] if arr[dst] != math.inf else -1