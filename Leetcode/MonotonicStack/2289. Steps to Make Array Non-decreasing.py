# 2289. Steps to Make Array Non-decreasing
# Might seen a little tricky take time to understand the approach and the question
# we maintain a decreasing stack 
# and a array where ith element means the nums of step reqd to remove the element
# the curr element will be removed after n + 1 steps where n is the max number of steps 
# reqd to remove a element in front of that element and lower than that element 
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        res = [0]*len(nums)
        for i,val in enumerate(nums):
            # print(stack,res)
            curr = 0
            while stack and stack[-1][0]<=val:
                q,prev = stack.pop()
                curr = max(curr,res[prev])
            if stack:
                res[i] = curr + 1
            stack.append([val,i])

        return max(res)
#[7,3,4,4,5,3,6]
#[0,1,2,3,4,1,5]

#[7,3,2,6,3,2,1]
#[0,1,1,2,1,1,1]

#[7,2,3,6,1,2,3,4]
#[0,1,2,3,1,2,3,4]