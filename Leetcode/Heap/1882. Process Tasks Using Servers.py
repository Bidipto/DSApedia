def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
    #we need to maintain two lists one of the free servers and other 
    #of the servers that are being used 
    
    #since we are to use the servers with the minimun weight and min index
    # we will use a min heap with weight,index,time 
    # we need to track time because of a special case 
    
    #also there is a special case where we dont have dont have any free servers 
    #in this case we have put the task in a queue for the server finishing the task first 
    
    #therefore we will use a min stack with the time,weight,index values
    
    free = [[weight, index, 0] for index, weight in enumerate(servers)]
    heapq.heapify(free)
    
    used = []
    res = []
    
    for i, taskLen in enumerate(tasks):
        while used and used[0][0]<=i or not free:
            time, weight, index = heapq.heappop(used)
            heapq.heappush(free, [weight, index, time])
            
        weight, index, time = heapq.heappop(free)
        heapq.heappush(used, [max(time,i)+taskLen, weight, index])
        res.append(index)
        
    return res