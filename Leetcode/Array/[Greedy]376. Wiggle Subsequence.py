#optimization to the dp solution 
def wiggleMaxLength(self, nums: List[int]) -> int:
    if len(nums) < 2: return len(nums)
    
    flag = None 
    res = 1
    
    for i in range(1, len(nums)):
        # True means we are looking for a peak
        if nums[i]>nums[i-1] and flag != True:
            flag = True
            res += 1
        
        elif nums[i]<nums[i-1] and flag != False:
            flag = False
            res += 1
            
    return res