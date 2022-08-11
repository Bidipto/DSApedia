# 238. Product of Array Except Self

def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(N) solution 
        N = len(nums)
        res = [1] * N 
        
        for i,val in enumerate(nums[:N-1]):
            res[i+1] *= val
            res[i+1] *= res[i]
            
        print(res)
            
        suffix = 1 
        for i in range(N-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res 