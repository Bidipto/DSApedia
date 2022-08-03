# 719. Find K-th Smallest Pair Distance

def smallestDistancePair(self, nums: List[int], k: int) -> int:
    #binary search on the answer space
    nums.sort()
    lo = 0
    hi = nums[-1]-nums[0]
    
    while lo<hi:
        mid = (lo+hi)//2
        
        #we will count the number of pairs less=<mid
        
        l = 0
        count = 0
        for r in range(len(nums)):
            while nums[r]-nums[l]>mid:
                l += 1
            count += (r-l)
        
        # print(hi,lo,mid,k)
        if count<k:
            lo = mid + 1
        else:
            hi = mid 
        
    return lo