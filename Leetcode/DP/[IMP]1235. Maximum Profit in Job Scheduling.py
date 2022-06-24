# 1235. Maximum Profit in Job Scheduling
# O(nlogn) DP + binary search in intervals 
# kafi mast problem
def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #first intuition is to sort the array 
        #there are two options to pick up the jobs
        #one: take the current job and the pick the another job after the current runtime
        #two: not take the current job 
        
        dp = dict()
        N = len(profit) 
        
        jobs = sorted([[startTime[i],endTime[i],profit[i]] for i in range(N)])
        startTime.sort()
        
        def magic(i):
            if i == N:
                return 0
            
            if i in dp:
                return dp[i]
            
            #not take 
            dp[i] = magic(i+1)
            
            #take 
            nextJob = bisect.bisect_left(startTime, jobs[i][1])
            dp[i] = max(dp[i], jobs[i][2] + magic(nextJob))
            
            return dp[i]
        
        return magic(0)