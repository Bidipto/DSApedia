# 2091. Removing Minimum and Maximum From Array
def minimumDeletions(self, nums: List[int]) -> int:
    #we have three options to remove the elements 
    #one from both side
    #two from start 
    #three from end
    #we actually dont care which index is of min and which is of max
    #what we care is which index is largers and which is smaller
    indexa = nums.index(min(nums))
    indexb = nums.index(max(nums))
    #swapping so that indexa always comes first 
    if indexb<indexa:
        indexa, indexb = indexb, indexa
    N = len(nums)
    #min of case1,2,3
    return min((indexa+1) + (N-indexb), indexb+1, N-indexa)