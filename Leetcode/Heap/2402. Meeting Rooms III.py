# 2402. Meeting Rooms III

def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
    free = [i for i in range(n)]
    heapq.heapify(free)
    res = collections.Counter()
    
    # heap with pairs (endTime,room)
    busy = []
    
    for start,end in sorted(meetings):
        # print(start,end,free,busy)
        while busy and busy[0][0]<=start:
            tempEnd,tempRoom = heapq.heappop(busy)
            heapq.heappush(free,tempRoom)
        
        if free:
            room = heapq.heappop(free)
            heapq.heappush(busy,(end,room))
        else:
            currEnd,room = heapq.heappop(busy)
            heapq.heappush(busy,(currEnd+(end-start),room))
        res[room] += 1
    #     print(room)
    # print(res)
    return res.most_common()[0][0]