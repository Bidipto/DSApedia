#diff is the amount of cost more required to send a person to the second city
#jitna chota cost utna faidemandh to send that person to city 2
def twoCitySchedCost(self, costs: List[List[int]]) -> int:   
    diff = [[i[1] - i[0],i[0],i[1]] for i in costs]
    heapq.heapify(diff)
    res = 0
    
    for i in range(len(costs)//2):
        res += heapq.heappop(diff)[2]
    for i in range(len(costs)//2):
        res += heapq.heappop(diff)[1]
    
    return res