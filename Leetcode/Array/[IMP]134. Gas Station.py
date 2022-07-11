def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #if the fuel is less than the total cost we cant make the trip
    if sum(gas)-sum(cost)<0:
        return -1
    
    surplus = 0
    start = 0
    for i in range(len(gas)):
        surplus += gas[i] - cost[i]
        if surplus<=0:
            start = i+1
            surplus = 0
            
    return start%len(gas)