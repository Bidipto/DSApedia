# 1955. Count Number of Special Subsequences
# there is a better solution using dp 


def countSpecialSubsequences(self, nums: List[int]) -> int:
    #we will use prev as last element we have taken into account 
    mod = pow(10,9) + 7
    dp = [[-1]*4 for i in range(len(nums))]
    
    def magic(i,prev):
        if i == len(nums):
            if prev == 2:
                return 1
            else:
                return 0
        if dp[i][prev] != -1:
            return dp[i][prev]
        
        res = 0
        #nottake 
        res += magic(i+1,prev)
        #take(if same element as prev)
        if nums[i] == prev:
            res += magic(i+1,prev)
        #take(if different element)
        if nums[i] == 0 and prev == -1:
            res += magic(i+1,0)
    
        elif nums[i] == 1 and prev == 0:
            res += magic(i+1,1)
        
        elif nums[i] == 2 and prev == 1:
            res += magic(i+1,2)
            
        dp[i][prev] = res%mod
        return dp[i][prev]
    
    return magic(0,-1)