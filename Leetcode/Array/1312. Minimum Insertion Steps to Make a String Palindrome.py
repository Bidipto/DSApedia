# 1312. Minimum Insertion Steps to Make a String Palindrome
def minInsertions(self, s: str) -> int:
    #modified palindrome subsequemce
    N = len(s)
    rs = s[::-1]
    
    dp = [[-1]*N for q in range(N)]
    
    def magic(m,n):
        if m == N or n == N:
            return 0
        
        if dp[m][n] != -1:
            return dp[m][n]
        
        if s[m] == rs[n]:
            dp[m][n] = 1 + magic(m+1,n+1)
        else:
            dp[m][n] = max(magic(m,n+1),magic(m+1,n))
            
        return dp[m][n]
    
    return N - magic(0,0)