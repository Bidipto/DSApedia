# 2025. Maximum Number of Ways to Partition an Array
from collections import defaultdict
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        #the idea is to create two dictionary one with all the runningsums
        #of index before the change another after and including the change
        pre = defaultdict(int)
        suf = defaultdict(int)
        running = []
        summ = sum(nums)
        N = len(nums)
        temp = 0
        for i in nums:
            temp += i
            running.append(temp)
            suf[temp] += 1
        
        # we cannt use the last valuse of the runnin sum
        # since the last element would be null
        # also we can chnage to k at the first index

        suf[summ] -= 1
        res = 0
        #when nothing is changed 
        if summ%2 == 0:
            res = suf[summ//2]
            
        #when we change to k
        for i in range(0,N):
            curr = 0
            #if number is equal to k the ans would be same as default
            if nums != k:
                newsumm = summ + (k - nums[i])
                #not possible if the summ is even
                if newsumm%2 == 0:
                    #we can only change at after 1,1 <= pivot < n
                    if i>0:
                        curr += pre[newsumm//2]
                    if i<N-1:
                        #since we are not updating the values 
                        #we have to search for the new sum value removing the change
                        curr += suf[(newsumm)//2-(k-nums[i])]
            res = max(res,curr)
            #suffix se prefix transfer
            pre[running[i]] += 1
            suf[running[i]] -= 1
        
        return res