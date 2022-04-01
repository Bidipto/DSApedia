#just implementation of lcs, aaah lcs is so f important
#just one condition we cant increment when the indexes are equal bass inta hi
#Lcs ka logic khun meh hona mangta hai

def LongestRepeatingSubsequence(self, s):
    M = len(s) #rows
    N = len(s)  #columns
    dp = [[-1 for i in range(N)] for j in range(M)]
    
    
    def magic(m, n, dp):
        if m == M:
            return 0
        if n == N:
            return 0
        
        if dp[m][n] != -1:
            return dp[m][n]
        
        if s[m] == s[n] and m != n:
            dp[m][n] = 1 + magic(m+1, n+1, dp)
        else:
            dp[m][n] = max(magic(m+1, n, dp),magic(m, n+1, dp))
        
        # print(dp, m, n)
        return dp[m][n]
        
    return magic(0, 0, dp)