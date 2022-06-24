# 1354. Construct Target Array With Multiple Sums

import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        N = len(target)
        #if len if the heap is one then its not possible usless the number is one
        if N == 1:
            return target[0] == 1
        
        heap = [-val for val in target]
        heapq.heapify(heap)
        summ = sum(target)
        
        #negative cause maxheap is used 
        #maxheap is used to store the largest elements 
        #and the simulations are done in repeat 
        
        #is naive approach with no multiplier(n) TlE is acheived 
        #so the concept of multiplier is used
        
        #qki technicalyy hum ek index pe restOfTheArray ka sum jodh rahe ha
        #toh we can take that out until that index is not the highest anymore 
        #that why we need the second largest element 
        while heap[0] != -1:
            # print(heap)
            largest = -heap[0]
            largest_2 = -heap[1]
            sumRest = summ - largest
            
            n = max(1,(largest-largest_2)//sumRest)
            # print(n,largest,largest_2,sumRest)
            
            largest -= sumRest*n
            
            summ = sumRest + largest
            heapq.heappushpop(heap, - largest)
            if largest<1: return False
        return True
            