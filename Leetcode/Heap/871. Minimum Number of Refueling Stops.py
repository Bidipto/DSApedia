# 871. Minimum Number of Refueling Stops

def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
    N = len(stations)
    stations.sort()
    
    heap = [-startFuel]
    stops = 0
    
    stops = -1
    i = 0 
    reach = 0
    
    while heap:
        # print(reach)
        reach += -heapq.heappop(heap)
        stops += 1
        if target<=reach:
            return stops 
        # print(reach,stations[i][0])
        while i<N and reach>=stations[i][0]:
            # print(reach,stations[i][0])
            heapq.heappush(heap,-stations[i][1])
            i += 1
    return -1