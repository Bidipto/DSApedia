from collections import deque
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #sliding window with unique elements 
        s = set()
        last = 0
        res = 0
        currsum = 0
        
        for i in nums:
            # print(sliding)
            if i in s:
                res = max(currsum,res)
                while True:
                    x = nums[last]
                    currsum -= x
                    s.remove(x)
                    if x == i:
                        break
                    last += 1
                last += 1
            s.add(i)
            currsum += i   
        
        return max(currsum,res)