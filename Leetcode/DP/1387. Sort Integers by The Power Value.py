#simple dimple dp
def getKth(self, lo: int, hi: int, k: int) -> int:
    dp = {1:0}
    
    def magic(i):
        # print(i)
        if i in dp:
            return dp[i]
        
        if i%2:
            dp[i] = 1 + magic((3*i)+1)
        else:
            dp[i] = 1 + magic(i//2)
            
        return dp[i]
    
    heap = []
    for i in range(lo, hi + 1 ):
        heapq.heappush(heap, [-(magic(i)),-i])
        # print(heap)
        if len(heap)>k:
            heapq.heappop(heap)
    
    return -heapq.heappop(heap)[1]