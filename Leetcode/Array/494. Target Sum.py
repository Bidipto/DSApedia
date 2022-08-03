from collections import Counter
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = Counter()
        res[0] = 1
        for val in nums:
            # print(res)
            temp = Counter()
            for key in res:
                temp[key + val] += res[key]
                temp[key - val] += res[key]
            
            res = temp
        return res[target] 