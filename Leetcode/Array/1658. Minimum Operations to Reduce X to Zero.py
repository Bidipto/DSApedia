# 1658. Minimum Operations to Reduce X to Zero
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        #insted of searching for the prefix and suffix sum x we search for the longest 
        #subarry of sum sum(arr) - x 
        lo = 0
        hi = 0
        currsum = 0
        target = sum(nums) - x
        res = -1
        
        while True:
            if hi == len(nums):
                break
            currsum += nums[hi]
            hi += 1
            while currsum>target and lo < hi:
                currsum -= nums[lo]
                lo += 1
            if currsum == target:
                res = max(res,hi-lo)
        
        
        return -1 if res == -1 else len(nums)-res