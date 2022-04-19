# 446. Arithmetic Slices II - Subsequence
# follow up t0 arithemetic slices 1
def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        N = len(nums)
        dp = [{} for i in range(N)]
        
        #dp table of dp[index of the element][gap]
        #dp[i][j] gives the number of subseq starting for i with gap j
         
        ## intitaly though of initailising dp[i][gap] with 0 when we find a gap 
        ## instead of using a default dict 
        ## ie now dp[i][gap] gives now of sub se with len atleast 2 instead 
        ## of what the answer demands
        # consider the exam [2,2,3,4]
        # if we do make a dp with min len of subseq then the answer would be 0
        # since it wount be able to differentiate between the first 2 and second 2
         
        ans = 0
        
        for i in range(N-1):
            for j in range(i+1,N):
                
                gap = nums[j] - nums[i]
                previous_counter = 0
                
                if gap in dp[i]:
                    previous_counter = dp[i][gap]
                    
                dp[j][gap] = dp[j].get(gap,0) + (previous_counter + 1)
                ans += previous_counter
                    
                # print(i,j,dp)
                    
        return ans