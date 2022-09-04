#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,val in enumerate(nums):
            if val in dic: return [dic[val],i]
            else: dic[target-val] = i
            
# @lc code=end

