# 1048. Longest String Chain
# a lot of optimizations pending 
def longestStrChain(self, words: List[str]) -> int:
    s = defaultdict(list)
    dp = dict()
    
    for word in words:
        s[len(word)].append(word)
    
    for i in range(16,0,-1):
        if i in s:
            maxx = i
            break
    
    def magic(w1):
        # print(s,w1)
        #base case 
        if not s:
            return 0
        
        #dp 
        if w1 in dp:
            return dp[w1]
        
        temp = 0
        for word in s[len(w1)+1]:
            if self.lcs(w1,word):
                # print(w1, word)
                temp = max(temp,1 + magic(word))
                            
        dp[w1] = temp
        return temp
    
    temp = 0
    
    for i in range(1,maxx+1):
        for val in s[i]:
            temp = max(temp,magic(val))
            if temp == maxx-1:
                break
    
    return temp + 1
                               
def lcs(self,w1,w2):
    M = len(w1)
    N = len(w2)
                            
    dp = [[-1]*N for q in range(M)]
                            
    def magic(m, n):
        if m == M or n == N:
            return 0
                            
        if dp[m][n] != -1:
            return dp[m][n]
        
        if w1[m] == w2[n]:
            dp[m][n] = 1 + magic(m+1,n+1)
        else:
            dp[m][n] = magic(m, n+1)
        
        return dp[m][n]
    
    res = magic(0,0)
    
    if res == min(M,N):
        return True
    else:
        return False