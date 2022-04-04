# 2216. Minimum Deletions to Make Array Beautiful
# lesson from the problem 
# looks for what we should return and excape unnessary jhamela
def minDeletion(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0    
    temp = 1
    start = 1
    res = 0
    while temp:
        temp = 0
        for i in range(start,len(nums),2):
            if nums[i] == nums[i-1]:
                temp = 1
                start = i + 1
                res += 1
                break
    if (len(nums) - res) % 2:
        res += 1
    return res