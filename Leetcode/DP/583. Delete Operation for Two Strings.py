# 583. Delete Operation for Two Strings
def minDistance(self, word1: str, word2: str) -> int:
    #lcs is the way to go 
    #read about a optimized lcs using only 1D dp array 
    #doest seem like the interviewer will expect such solutions
    #but good to know, implement that 
    M = len(word1)
    N = len(word2)
    
    dp = [[-1]*N for q in range(M)]
    
    def magic(m,n):
        if m == M:
            return 0
        if n == N:
            return 0
        
        if dp[m][n] != -1:
            return dp[m][n]
        
        if word1[m] == word2[n]:
            dp[m][n] = 1 + magic(m+1,n+1)
        else:
            dp[m][n] = max(magic(m+1,n),magic(m,n+1))
            
        return dp[m][n]
    
    
    return M + N - (2*magic(0,0))
