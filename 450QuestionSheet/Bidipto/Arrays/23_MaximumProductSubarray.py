def maxProduct(self, nums: List[int]) -> int:
    currmax = 1
    currmin = 1
    res = max(nums)
    #we need to keep track of the lowest subarray and highest cause
    #if a negative number pops, the lowest subarray product will become highest
    
    #and we need i(the first arg in min and max) to remove 0s when it come 
    for i in nums:
        temp = currmax * i
        currmax = max(i , currmax * i, currmin * i)
        currmin = min(i , temp, currmin * i)
        
        res = max(res, currmax)
    
    return res