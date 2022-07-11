# 2333. Minimum Sum of Squared Difference
# worked up a 3dp and 2dp solution before coming up to the heap solution
def minSumSquareDiff(self, nums1: List[int], nums2: List[int], K1: int, K2: int) -> int:
    N = len(nums1)
    heap = [-abs(nums1[i] - nums2[i]) for i in range(N)]
    s = -sum(heap)
    heapq.heapify(heap)
    K = K1 + K2
    
    if K>=s:
        return 0
    if len(heap) == 1:
        return pow(heap[1]-K,2)
    
    while K:
        t1 = -heapq.heappop(heap)
        t2 = -heap[0]
        diff = t1-t2
        maxx = min(K,max(K//N,diff,1))
        t1 -= maxx
        K -= maxx
        heapq.heappush(heap,-t1)
        
    # print(heap)
    return sum([pow(i,2) for i in heap])