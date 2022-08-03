# 1911. Maximum Alternating Subsequence Sum

def maxAlternatingSum(self, nums: List[int]) -> int:
        #memory optimizationzz
        odd = 0
        even = 0
        for i in nums:
            odd = max(odd,even-i)
            even = max(even,odd+i)
            
        return max(odd,even)