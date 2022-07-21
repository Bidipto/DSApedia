# 1696. Jump Game VI
# instead of a regualar dp solution which a also possible and we get a TLE
# we can use a heap to solve this problem and traverse from the end, similar to dijsktra algo
def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        if N == 1:
            return nums[0]
        
        dp = [math.inf for i in range(N)]
        
        heap = []
        heap.append((-nums[-1],N-1))
        
        for i in range(N-2,0,-1):
            while heap and heap[0][1]>i+k:
                heapq.heappop(heap)
                
            val = -heap[0][0]
            heapq.heappush(heap,(-(nums[i]+val),i))
            
        while heap and heap[0][1]>k:
            heapq.heappop(heap)
            
        return nums[0] - heap[0][0]