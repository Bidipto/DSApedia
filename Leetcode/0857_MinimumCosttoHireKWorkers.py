#initial intuition similar to 1383. Maximum Performance of a Team
#https://leetcode.com/problems/maximum-performance-of-a-team
#looks like a heap solution, highly recommended to solve the  maximum performance of a team problem first
#target is to pay the least amount of money to hire the k workers
#ratio of wage to quality is the key to solve this problem ie the least money per quality we have to pay for K workers
#therefore we need to have the least [sum of quality of k workers * max ratio of wage to quality among them to satisfy everyone]
#sort the workers by ratio of wage to quality, and then looping through the array,
# storing the best k workers in a heap and then updating the res with the min value of possible answer every time

#Edge case or a possible fault in the solution
#what if the quality added is the max quality and the its removed from the loop in the same iteration, 
#we still mutiply the ration of the popped element
#this doesnt pose a problem cause the ratios are sorted, and the we would have already multiplied with a samller ratio in previous iterations


def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
    arr = sorted([[float(w)/q, q] for w,q in zip(wage, quality)])
    
    sumquality = 0
    res = math.inf
    maxheap = []
    for ratio, qua in arr:
        heapq.heappush(maxheap, -qua)
        sumquality += qua
        if len(maxheap) > k:
            #since the number is already negative in the maxheap, if we add to the sum we are substrating it 
            # print(maxheap)
            sumquality += heapq.heappop(maxheap)
        
        if len(maxheap) == k:
            res = min(res, sumquality * ratio)
    return res