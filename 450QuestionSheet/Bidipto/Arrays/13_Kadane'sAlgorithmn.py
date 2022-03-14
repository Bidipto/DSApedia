#just a small modification from the largest sum subarray problem
#because this requires atleast 1 element in the subarray
def maxSubArraySum(self,nums,N):
        tsum=0
        maxi=nums[0]
        for i in nums:
            tsum = i + max(0, tsum)
            maxi=max(maxi,tsum)
        return maxi
