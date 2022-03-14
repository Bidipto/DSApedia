def maxSubArray(self, nums):
        #KAYDANE's algo
        
        tsum=0
        maxi=nums[0]
        for i in nums:
            tsum = i + max(0, tsum)
            maxi=max(maxi,tsum)
        return maxi
        '''
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        print(nums)
        return max(nums)
        '''