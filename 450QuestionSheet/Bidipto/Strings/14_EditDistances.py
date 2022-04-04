#kafi sahi question 
#again based on lcs
#also insertion and deletion is the same thing
#snake matrix visualisation 

def editDistance(self, text1, text2):
    M = len(text1) #rows
    N = len(text2)  #columns
    dp = [[-1 for i in range(N)] for j in range(M)]
    
    
    def magic(m, n, dp):
        if m == M and n == N:
            return 0
        elif m == M:
            return N-n
        elif n == N:
            return M-m
        
        if dp[m][n] != -1:
            return dp[m][n]
        
        if text1[m] == text2[n]:
            dp[m][n] = magic(m+1, n+1, dp)
        else:
            dp[m][n] = 1 + min(magic(m+1, n, dp),magic(m, n+1, dp),magic(m+1, n+1, dp))
        
        # print(dp, m, n)
        return dp[m][n]
        
    return magic(0, 0, dp)