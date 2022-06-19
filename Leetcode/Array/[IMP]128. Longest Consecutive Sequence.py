# 128. Longest Consecutive Sequence
#we make an set for the array given fro faster look up time 
#and we only start check if that number is the first consequtive number in the ar 
def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in nums:
            if i-1 not in s:
                freq = 1
                while i+1 in s:
                    freq+=1
                    i+=1
                    
                res = max(res,freq)
                
        return res